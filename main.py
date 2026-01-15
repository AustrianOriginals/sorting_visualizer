import random
import matplotlib.pyplot as plt
import time

# Generate random data
original_data = [random.randint(1, 100) for _ in range(20)]

data_bubble = original_data.copy()
data_minimal = original_data.copy()
data_insertion = original_data.copy()

def bubble_sort(data_bubble, bubble_steps):
    for i in range(len(data_bubble)):
        for j in range(0, len(data_bubble)-i-1):
            bubble_steps[0] += 1
            if data_bubble[j] > data_bubble[j+1]:
                data_bubble[j], data_bubble[j+1] = data_bubble[j+1], data_bubble[j]
                yield data_bubble

def minimal_sort(data_minimal, selection_steps):
    for i in range(len(data_minimal)):
        min_idx = i
        for j in range(i+1, len(data_minimal)):
            selection_steps[0] += 1
            if data_minimal[j] < data_minimal[min_idx]:
                min_idx = j
        data_minimal[i], data_minimal[min_idx] = data_minimal[min_idx], data_minimal[i]
        yield data_minimal

def insertion_sort(data_insertion, insertion_steps):
    for i in range(1, len(data_insertion)):
        key = data_insertion[i]
        j = i-1
        while j >=0 and key < data_insertion[j]:
            insertion_steps[0] += 1
            data_insertion[j + 1] = data_insertion[j]
            j -= 1
        data_insertion[j + 1] = key
        yield data_insertion

plt.ion()
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

bubble_steps = [0]
selection_steps = [0]
insertion_steps = [0]

bubble_gen = bubble_sort(data_bubble, bubble_steps)
selection_gen = minimal_sort(data_minimal, selection_steps)
insertion_gen = insertion_sort(data_insertion, insertion_steps)

while True:
    updated = False

    for ax, gen, data, title, steps in [
        (axs[0], bubble_gen, data_bubble, "Bubble Sort", bubble_steps),
        (axs[1], selection_gen, data_minimal, "Selection Sort", selection_steps),
        (axs[2], insertion_gen, data_insertion, "Insertion Sort", insertion_steps),
    ]:
        try:
            next(gen)
            ax.clear()
            ax.bar(range(len(data)), data)
            ax.set_title(f"{title} | Steps: {steps[0]}")
            updated = True
        except StopIteration:
            ax.set_title(f"{title} | Steps: {steps[0]} (Done)")

    plt.pause(0.1)