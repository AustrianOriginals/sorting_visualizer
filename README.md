# 📊 Python Sorting Algorithm Visualizer

A Python-based interactive visualization tool for comparing sorting algorithms side by side.  
This project visually demonstrates how different algorithms work, how many steps they take, and how their theoretical time complexities compare in practice.

---

## 🚀 Features

- 🔍 **Side-by-side comparison** of multiple sorting algorithms  
- 📈 **Live bar-chart visualization** using Matplotlib  
- 🔢 **Step counters** to track algorithm operations  
- ⏱ **Execution time measurement** per algorithm  
- 📐 **Big-O time complexity display**  
- 🔄 **Reset button** to generate new random datasets  
- 🎓 Designed for **learning, teaching, and experimentation**

---

## 🧠 Implemented Algorithms

| Algorithm        | Best Case | Average Case | Worst Case |
|------------------|-----------|--------------|------------|
| Bubble Sort      | O(n)      | O(n²)        | O(n²)     |
| Selection Sort   | O(n²)     | O(n²)        | O(n²)     |
| Insertion Sort   | O(n)      | O(n²)        | O(n²)     |

Each algorithm runs on the **same initial dataset** to ensure a fair comparison.

---

## 🖥️ How It Works

- Random data is generated and visualized as vertical bars
- Each algorithm is implemented as a **Python generator**
- Algorithms advance **one meaningful step at a time**
- The visualization updates after every step
- Step counts and execution time are displayed live
- Finished algorithms freeze while others continue

This approach makes algorithm behavior easy to observe and compare.

---

## 📦 Requirements

- Python 3.8+
- matplotlib

Install dependencies with:

```bash
pip install matplotlib
