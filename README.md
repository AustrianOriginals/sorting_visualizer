# Sorting Algorithm Visualizer (Python)

A lightweight desktop visualization tool that compares core sorting algorithms side by side using Matplotlib.

This application is designed for education, demos, and internal technical presentations where algorithm behavior, operation count, and runtime progression need to be shown clearly.

---

## Overview

The visualizer renders six synchronized bar charts from the same randomly generated dataset:

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort

Each algorithm runs independently as a generator, allowing step-by-step updates in real time while preserving visual comparability.

---

## Current Capabilities

- Side-by-side live visualization for 6 sorting algorithms
- Shared input dataset for fair comparison
- Real-time operation (step) counters
- Real-time write operation tracking
- Real-time elapsed time display per algorithm
- Big-O notation shown in each chart title
- Reset control to generate a new dataset and restart all algorithms
- Color-coded charts for easy identification
- 2x3 grid layout for optimal viewing

---

## Algorithm Complexity Reference

| Algorithm | Best | Average | Worst |
|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) |
| Selection Sort | O(n²) | O(n²) | O(n²) |
| Insertion Sort | O(n) | O(n²) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) |

> Note: The UI displays simplified complexity labels taken from the script constants.

---

## Technical Notes

- Built with Python 3.12+ and Matplotlib interactive mode (`plt.ion()`)
- Clean architecture with dataclasses (`SortMetrics`, `AlgorithmState`)
- Update loop advances each generator one step per frame (`plt.pause(0.02)`)
- Step counters track comparison operations, write counters track array modifications
- Elapsed time measured using `time.perf_counter()`
- Type hints throughout for maintainability
- Modular design for easy algorithm addition

---

## Requirements

- Python 3.8+
- matplotlib

Install dependency:

```bash
pip install matplotlib
```

---

## Run

From the project root, execute:

```bash
python main.py
```

---

## Usage

1. Launch the app.
2. Observe the six sorting panels (2x3 grid) updating in parallel.
3. Review each panel title for:
   - Algorithm name
   - Big-O reference
   - Current status (Running/Done)
   - Step count (comparisons)
   - Write count (array modifications)
   - Elapsed runtime
4. Click **Reset Dataset** to generate a new random dataset and restart all algorithms.
5. Close the window to exit the application.
## Project Structure

```text
sorting_visualizer/
├── main.py
└── README.md
```

---

## Intended Use

- Classroom demonstrations
- Interview prep and algorithm walkthroughs
- Internal engineering knowledge-sharing sessions

---

## Future Enhancements (Recommended)

- Add configurable dataset size slider
- Add speed control (animation delay adjustment)
- Add pause/resume and single-step mode
- Add additional algorithms (Radix, Shell, Cocktail, Comb)
- Export benchmark results to CSV or JSON
- Add ability to load custom datasets
- Package as an executable for non-technical users
- Add color highlighting for active comparisons/swaps

---

## License

Use and modify freely for learning and demonstration purposes.
