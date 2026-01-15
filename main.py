import random
import matplotlib.pyplot as plt
import time

# Generate random data
data = [random.randint(1, 100) for _ in range(20)]

# Create a bar chart
plt.bar(range(len(data)), data)
plt.show()

def bubble_sort(data):
    for i in range(len(data)):
        for j in range(0, len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                yield data

def minimal_sort(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        yield data

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >=0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        yield data

plt.ion()
fig, ax = plt.subplots()

#Bubble Sort Visualization
#for step in bubble_sort(data):
    #ax.clear()
    #ax.bar(range(len(step)), step)
    #plt.pause(0.1)

# Minimal Sort Visualization
#for step in minimal_sort(data):
    #ax.clear()
    #ax.bar(range(len(step)), step)
    #plt.pause(0.1)

for step in insertion_sort(data):
    ax.clear()
    ax.bar(range(len(step)), step)
    plt.pause(0.1)

plt.ioff()
plt.show()
