from __future__ import annotations

import random
import time
from dataclasses import dataclass, field
from typing import Callable, Generator

import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# -----------------------------
# Configuration
# -----------------------------
DATASET_SIZE = 100
DATA_MIN_VALUE = 1
DATA_MAX_VALUE = 100
FRAME_DELAY_SECONDS = 0.02


@dataclass
class SortMetrics:
    """Runtime metrics collected for each sorting algorithm."""

    steps: int = 0
    writes: int = 0
    elapsed_seconds: float = 0.0
    _start_time: float = field(default=0.0, repr=False)

    def start(self) -> None:
        self._start_time = time.perf_counter()

    def tick(self) -> None:
        self.elapsed_seconds = time.perf_counter() - self._start_time

    def stop(self) -> None:
        self.tick()


@dataclass
class AlgorithmState:
    """State required to animate one sorting algorithm."""

    name: str
    big_o: str
    color: str
    sorter: Callable[[list[int], SortMetrics], Generator[None, None, None]]
    data: list[int] = field(default_factory=list)
    metrics: SortMetrics = field(default_factory=SortMetrics)
    generator: Generator[None, None, None] | None = None
    finished: bool = False

    def reset(self, source_data: list[int]) -> None:
        self.data = source_data.copy()
        self.metrics = SortMetrics()
        self.metrics.start()
        self.generator = self.sorter(self.data, self.metrics)
        self.finished = False

    def advance(self) -> None:
        if self.finished or self.generator is None:
            return
        try:
            next(self.generator)
            self.metrics.tick()
        except StopIteration:
            self.finished = True
            self.metrics.stop()


# -----------------------------
# Sorting algorithms (generators)
# -----------------------------
def bubble_sort(data: list[int], metrics: SortMetrics) -> Generator[None, None, None]:
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            metrics.steps += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                metrics.writes += 2
                swapped = True
                yield
        if not swapped:
            break


def selection_sort(data: list[int], metrics: SortMetrics) -> Generator[None, None, None]:
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            metrics.steps += 1
            if data[j] < data[min_index]:
                min_index = j
        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
            metrics.writes += 2
            yield


def insertion_sort(data: list[int], metrics: SortMetrics) -> Generator[None, None, None]:
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0:
            metrics.steps += 1
            if data[j] <= key:
                break
            data[j + 1] = data[j]
            metrics.writes += 1
            j -= 1
            yield
        data[j + 1] = key
        metrics.writes += 1
        yield


def merge_sort(data: list[int], metrics: SortMetrics) -> Generator[None, None, None]:
    n = len(data)
    temp = [0] * n
    width = 1

    while width < n:
        for left in range(0, n, 2 * width):
            mid = min(left + width, n)
            right = min(left + 2 * width, n)

            i, j, k = left, mid, left

            while i < mid and j < right:
                metrics.steps += 1
                if data[i] <= data[j]:
                    temp[k] = data[i]
                    i += 1
                else:
                    temp[k] = data[j]
                    j += 1
                k += 1
                metrics.writes += 1
                yield

            while i < mid:
                temp[k] = data[i]
                i += 1
                k += 1
                metrics.writes += 1
                yield

            while j < right:
                temp[k] = data[j]
                j += 1
                k += 1
                metrics.writes += 1
                yield

            for index in range(left, right):
                data[index] = temp[index]
                metrics.writes += 1
                yield

        width *= 2


def quick_sort(data: list[int], metrics: SortMetrics) -> Generator[None, None, None]:
    if len(data) < 2:
        return

    stack: list[tuple[int, int]] = [(0, len(data) - 1)]

    while stack:
        low, high = stack.pop()
        if low >= high:
            continue

        pivot = data[high]
        i = low - 1

        for j in range(low, high):
            metrics.steps += 1
            if data[j] <= pivot:
                i += 1
                if i != j:
                    data[i], data[j] = data[j], data[i]
                    metrics.writes += 2
                    yield

        pivot_index = i + 1
        if pivot_index != high:
            data[pivot_index], data[high] = data[high], data[pivot_index]
            metrics.writes += 2
            yield

        # Push larger partition first to reduce stack depth.
        left = (low, pivot_index - 1)
        right = (pivot_index + 1, high)

        left_size = left[1] - left[0]
        right_size = right[1] - right[0]

        if left_size > right_size:
            if left[0] < left[1]:
                stack.append(left)
            if right[0] < right[1]:
                stack.append(right)
        else:
            if right[0] < right[1]:
                stack.append(right)
            if left[0] < left[1]:
                stack.append(left)


def heap_sort(data: list[int], metrics: SortMetrics) -> Generator[None, None, None]:
    def sift_down(start: int, end: int) -> Generator[None, None, None]:
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break

            if child + 1 <= end:
                metrics.steps += 1
                if data[child] < data[child + 1]:
                    child += 1

            metrics.steps += 1
            if data[root] >= data[child]:
                break

            data[root], data[child] = data[child], data[root]
            metrics.writes += 2
            root = child
            yield

    n = len(data)
    for start in range((n - 2) // 2, -1, -1):
        yield from sift_down(start, n - 1)

    for end in range(n - 1, 0, -1):
        data[end], data[0] = data[0], data[end]
        metrics.writes += 2
        yield
        yield from sift_down(0, end - 1)


def generate_dataset() -> list[int]:
    return [random.randint(DATA_MIN_VALUE, DATA_MAX_VALUE) for _ in range(DATASET_SIZE)]


def draw_algorithm(ax: plt.Axes, algorithm: AlgorithmState) -> None:
    ax.clear()
    ax.bar(range(len(algorithm.data)), algorithm.data, color=algorithm.color, edgecolor="black", linewidth=0.2)
    ax.set_xticks([])
    ax.set_yticks([])
    status = "Done" if algorithm.finished else "Running"
    ax.set_title(
        (
            f"{algorithm.name} ({algorithm.big_o})\n"
            f"Status: {status} | Steps: {algorithm.metrics.steps} | "
            f"Writes: {algorithm.metrics.writes} | Time: {algorithm.metrics.elapsed_seconds:.4f}s"
        ),
        fontsize=9,
    )


def build_algorithms() -> list[AlgorithmState]:
    return [
        AlgorithmState("Bubble Sort", "O(n²)", "#4C78A8", bubble_sort),
        AlgorithmState("Selection Sort", "O(n²)", "#F58518", selection_sort),
        AlgorithmState("Insertion Sort", "O(n²) avg / O(n) best", "#54A24B", insertion_sort),
        AlgorithmState("Merge Sort", "O(n log n)", "#E45756", merge_sort),
        AlgorithmState("Quick Sort", "O(n log n) avg / O(n²) worst", "#72B7B2", quick_sort),
        AlgorithmState("Heap Sort", "O(n log n)", "#B279A2", heap_sort),
    ]


def main() -> None:
    plt.ion()

    algorithms = build_algorithms()
    shared_data = generate_dataset()
    for algorithm in algorithms:
        algorithm.reset(shared_data)

    fig, axes = plt.subplots(2, 3, figsize=(18, 9))
    fig.suptitle("Sorting Algorithm Visualizer", fontsize=16, fontweight="bold")
    axes_flat = axes.flatten()

    reset_ax = plt.axes([0.42, 0.01, 0.16, 0.05])
    reset_button = Button(reset_ax, "Reset Dataset")

    def on_reset(_: object) -> None:
        new_data = generate_dataset()
        for algorithm in algorithms:
            algorithm.reset(new_data)

    reset_button.on_clicked(on_reset)

    try:
        fig.tight_layout(rect=[0.02, 0.07, 0.98, 0.95])
    except Exception:
        pass  # Suppress tight_layout warning with button widget

    while plt.fignum_exists(fig.number):
        for axis, algorithm in zip(axes_flat, algorithms):
            algorithm.advance()
            draw_algorithm(axis, algorithm)

        plt.pause(FRAME_DELAY_SECONDS)


if __name__ == "__main__":
    main()