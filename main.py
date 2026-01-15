import random
import matplotlib.pyplot as plt
import time

#Initialize time variables
bubble_time = [0.0]
selection_time = [0.0]
insertion_time = [0.0]

#initialize step counters
bubble_steps = [0]
selection_steps = [0]
insertion_steps = [0]

# Generate random data
original_data = [random.randint(1, 100) for _ in range(20)]

data_bubble = original_data.copy()
data_minimal = original_data.copy()
data_insertion = original_data.copy()

def bubble_sort(data, steps, elapsed):
    start = time.perf_counter()
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            steps[0] += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                yield
    elapsed[0] = time.perf_counter() - start


def minimal_sort(data_minimal, selection_steps, elapsed):
    start = time.perf_counter()
    for i in range(len(data_minimal)):
        min_idx = i
        for j in range(i+1, len(data_minimal)):
            selection_steps[0] += 1
            if data_minimal[j] < data_minimal[min_idx]:
                min_idx = j
        data_minimal[i], data_minimal[min_idx] = data_minimal[min_idx], data_minimal[i]
        yield data_minimal
    elapsed[0] = time.perf_counter() - start

def insertion_sort(data_insertion, insertion_steps, elapsed):
    start = time.perf_counter()
    for i in range(1, len(data_insertion)):
        key = data_insertion[i]
        j = i-1
        while j >=0 and key < data_insertion[j]:
            insertion_steps[0] += 1
            data_insertion[j + 1] = data_insertion[j]
            j -= 1
        data_insertion[j + 1] = key
        yield data_insertion
    elapsed[0] = time.perf_counter() - start

plt.ion()
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

#initialize iterators
bubble_gen = bubble_sort(data_bubble, bubble_steps, bubble_time)
selection_gen = minimal_sort(data_minimal, selection_steps, selection_time)
insertion_gen = insertion_sort(data_insertion, insertion_steps, insertion_time)
elapsed = [0.0, 0.0, 0.0]

while True:
    updated = False

    for ax, gen, data, title, steps, elapsed in [
        (axs[0], bubble_gen, data_bubble, "Bubble Sort", bubble_steps, bubble_time),
        (axs[1], selection_gen, data_minimal, "Selection Sort", selection_steps, selection_time),
        (axs[2], insertion_gen, data_insertion, "Insertion Sort", insertion_steps, insertion_time),
    ]:
        try:
            next(gen)
            ax.clear()
            ax.bar(range(len(data)), data)
            ax.set_title(f"{title}\nSteps: {steps[0]} | Time: {elapsed[0]:.2f}s")
            updated = True
        except StopIteration:
            ax.set_title(f"{title} (Done)\nSteps: {steps[0]} | Time: {elapsed[0]:.2f}s")
    plt.pause(0.1)