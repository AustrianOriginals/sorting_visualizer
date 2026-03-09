# Sorting Algorithm Visualizer (Python)

A lightweight desktop visualization tool that compares core sorting algorithms side by side using Matplotlib.

This application is designed for education, demos, and internal technical presentations where algorithm behavior, operation count, and runtime progression need to be shown clearly.

---

## Overview

The visualizer renders three synchronized bar charts from the same randomly generated dataset:

- Bubble Sort
- Selection Sort
- Insertion Sort

Each algorithm runs independently as a generator, allowing step-by-step updates in real time while preserving visual comparability.

---

## Current Capabilities

- Side-by-side live visualization for 3 sorting algorithms
- Shared input dataset for fair comparison
- Real-time operation (step) counters
- Real-time elapsed time display per algorithm
- Big-O notation shown in each chart title
- Reset control to generate a new dataset and restart all algorithms

---

## Algorithm Complexity Reference

| Algorithm | Best | Average | Worst |
|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) |
| Selection Sort | O(n²) | O(n²) | O(n²) |
| Insertion Sort | O(n) | O(n²) | O(n²) |

> Note: The UI displays simplified complexity labels taken from the script constants.

---

## Technical Notes

- Built with Python and Matplotlib interactive mode (`plt.ion()`)
- Update loop advances each generator one step per frame (`plt.pause(0.1)`)
- Step counters are incremented during key operations in each algorithm implementation
- Elapsed time is measured using `time.perf_counter()`

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
2. Observe the three sorting panels updating in parallel.
3. Review each panel title for:
	- Algorithm name
	- Big-O reference
	- Current step count
	- Elapsed runtime
4. Click **Reset** to generate a new random dataset and restart all algorithms.

---

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

- Add additional algorithms (Merge, Quick, Heap)
- Add configurable dataset size and speed controls
- Add pause/resume and single-step mode
- Export benchmark results to CSV
- Package as an executable for non-technical users

---

## License

Use and modify freely for learning and demonstration purposes.
