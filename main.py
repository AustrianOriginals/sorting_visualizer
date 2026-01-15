import random
import matplotlib.pyplot as plt
import time

# Generate random data
original_data = [random.randint(1, 100) for _ in range(20)]

# Create a bar chart
#plt.bar(range(len(original_data)), original_data)
#plt.show()

data_bubble = original_data.copy()
data_minimal = original_data.copy()
data_insertion = original_data.copy()

def bubble_sort(data_bubble):
    for i in range(len(data_bubble)):
        for j in range(0, len(data_bubble)-i-1):
            if data_bubble[j] > data_bubble[j+1]:
                data_bubble[j], data_bubble[j+1] = data_bubble[j+1], data_bubble[j]
                yield data_bubble

def minimal_sort(data_minimal):
    for i in range(len(data_minimal)):
        min_idx = i
        for j in range(i+1, len(data_minimal)):
            if data_minimal[j] < data_minimal[min_idx]:
                min_idx = j
        data_minimal[i], data_minimal[min_idx] = data_minimal[min_idx], data_minimal[i]
        yield data_minimal

def insertion_sort(data_insertion):
    for i in range(1, len(data_insertion)):
        key = data_insertion[i]
        j = i-1
        while j >=0 and key < data_insertion[j]:
            data_insertion[j + 1] = data_insertion[j]
            j -= 1
        data_insertion[j + 1] = key
        yield data_insertion

plt.ion()
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

bubble_gen = bubble_sort(data_bubble)
selection_gen = minimal_sort(data_minimal)
insertion_gen = insertion_sort(data_insertion)

while True:
    updated = False

    for ax, gen, data, title in [
        (axs[0], bubble_gen, data_bubble, "Bubble Sort"),
        (axs[1], selection_gen, data_minimal, "Selection Sort"),
        (axs[2], insertion_gen, data_insertion, "Insertion Sort"),
    ]:
        try:
            next(gen)
            ax.clear()
            ax.bar(range(len(data)), data)
            ax.set_title(title)
            updated = True
        except StopIteration:
            pass

    if not updated:
        break

    plt.pause(0.1)