# Sorting Algorithm Benchmark Tool

A Python tool for benchmarking various sorting algorithms on text files. This tool provides performance metrics and comparisons between different sorting algorithms.

## :dart: Features

- Benchmark multiple sorting algorithms on text data
- Visualize sorting progress with progress bars
- Generate comprehensive performance comparisons
- Support for file output of sorted data
- Adaptable to different types of text inputs

## Supported Algorithms

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort
- Radix Sort
- Counting Sort
- Shell Sort
- Bucket Sort

## :hammer_and_wrench: Installation

1. Clone this repository:

```bash
git clone https://github.com/thealper2/sorting-algorithm-benchmark.git
cd sorting-algorithm-benchmark
```

2. Install required dependencies:

```bash
pip install rich
```

## :joystick: Usage

### Basic Usage

Run the benchmark on a text file:

```bash
python benchmark.py data.txt
```

This will run all sorting algorithms on the specified file and display a comparison table.

### Specific Algorithm

To benchmark a specific algorithm:

```bash
python benchmark.py data.txt -a quick
```

### Save Sorted Output

To save the sorted output to a file:

```bash
python benchmark.py data.txt -o
```

When benchmarking all algorithms, this will save the result from the fastest algorithm.

### Command-line Arguments

- `file`: Path to the text file to sort (required)
- `-a, --algorithm`: Specific algorithm to benchmark (optional)
- `-o, --output`: Save sorted output to file (optional)

## :clipboard: Example Output

```bash
Reading file: data.txt
Read 10000 lines from file.

Starting benchmarks...

Benchmarking bubble: ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100%
Bubble completed in 2.34 s

Benchmarking quick: ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100%
Quick completed in 45.67 ms

Performance Comparison:
┏━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Algorithm   ┃ Time     ┃ Relative Performance  ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ quick       │ 45.67 ms │ Fastest 🥇            │
│ bubble      │ 2.34 s   │ 51.24x slower         │
├─────────────┼──────────┼───────────────────────┤
│ Average Time│ 1.19 s   │                       │
│ Median Time │ 1.19 s   │                       │
└─────────────┴──────────┴───────────────────────┘
```

## :scroll: License

MIT License