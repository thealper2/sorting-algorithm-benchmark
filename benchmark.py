#!/usr/bin/env python3
"""
Algorithm Benchmark Tool

This script benchmarks various sorting algorithms on text files.
It supports multiple algorithms and provides performance metrics.
"""

import os
import time
import argparse
import statistics
from typing import List, Dict, Any, Union, Callable
from rich.console import Console
from rich.progress import (
    Progress,
    TextColumn,
    BarColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)
from rich.table import Table
import importlib
import sys
from pathlib import Path

# Configure Rich console
console = Console()


def format_time(seconds: float) -> str:
    """
    Format time in appropriate units (ns, μs, ms, s)

    Args:
        seconds: Time in seconds

    Returns:
        Formatted time string with appropriate unit
    """
    if seconds < 1e-6:  # Less than 1 microsecond
        return f"{seconds * 1e9:.2f} ns"
    elif seconds < 1e-3:  # Less than 1 millisecond
        return f"{seconds * 1e6:.2f} μs"
    elif seconds < 1:  # Less than 1 second
        return f"{seconds * 1e3:.2f} ms"
    else:
        return f"{seconds:.2f} s"


def read_file(filename: str) -> List[str]:
    """
    Read text file and return lines as a list

    Args:
        filename: Path to the text file

    Returns:
        List of strings from the file
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        console.print(f"[bold red]Error:[/bold red] File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] Failed to read file: {str(e)}")
        sys.exit(1)


def write_file(filename: str, data: List[str]) -> None:
    """
    Write sorted data to a file

    Args:
        filename: Output file name
        data: Sorted list of strings
    """
    try:
        output_dir = Path("sorted_output")
        output_dir.mkdir(exist_ok=True)

        with open(output_dir / filename, "w", encoding="utf-8") as file:
            for line in data:
                file.write(f"{line}\n")
        console.print(
            f"[green]Sorted data saved to[/green] [bold]sorted_output/{filename}[/bold]"
        )
    except Exception as e:
        console.print(
            f"[bold red]Error:[/bold red] Failed to write output file: {str(e)}"
        )


def get_available_algorithms() -> List[str]:
    """
    Get list of available sorting algorithms from the sorting directory

    Returns:
        List of algorithm names
    """
    algorithms = []
    sorting_dir = Path("sorting")

    if not sorting_dir.exists():
        console.print("[bold red]Error:[/bold red] 'sorting' directory doesn't exist.")
        sys.exit(1)

    for file in sorting_dir.glob("*.py"):
        if file.name != "__init__.py" and not file.name.startswith("_"):
            algorithms.append(file.stem)

    return algorithms


def load_algorithm(name: str) -> Callable[[List[str]], List[str]]:
    """
    Dynamically load a sorting algorithm module

    Args:
        name: Name of the algorithm

    Returns:
        Sorting function
    """
    try:
        module = importlib.import_module(f"sorting.{name}")
        return module.sort
    except ImportError:
        console.print(
            f"[bold red]Error:[/bold red] Algorithm '{name}' not found in the sorting directory."
        )
        sys.exit(1)
    except AttributeError:
        console.print(
            f"[bold red]Error:[/bold red] Algorithm '{name}' does not have a 'sort' function."
        )
        sys.exit(1)


def benchmark_algorithm(
    algorithm: str, data: List[str]
) -> Dict[str, Union[float, List[str]]]:
    """
    Benchmark a single sorting algorithm

    Args:
        algorithm: Name of the algorithm
        data: Data to sort

    Returns:
        Dictionary with results including time taken and sorted data
    """
    # Make a copy of the data to avoid modifying the original
    data_copy = data.copy()

    sort_fn = load_algorithm(algorithm)

    with Progress(
        TextColumn(f"[bold blue]Benchmarking {algorithm}:[/bold blue]"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeElapsedColumn(),
        TimeRemainingColumn(),
        console=console,
    ) as progress:
        # Create a task for visual feedback
        task = progress.add_task(f"Sorting with {algorithm}", total=1)

        # Measure execution time
        start_time = time.perf_counter()
        sorted_data = sort_fn(data_copy)
        end_time = time.perf_counter()

        progress.update(task, completed=1)

    execution_time = end_time - start_time

    return {"algorithm": algorithm, "time": execution_time, "sorted_data": sorted_data}


def run_all_benchmarks(data: List[str], algorithms: List[str]) -> List[Dict[str, Any]]:
    """
    Run benchmarks for all algorithms

    Args:
        data: Data to sort
        algorithms: List of algorithms to benchmark

    Returns:
        List of benchmark results
    """
    results = []

    for algorithm in algorithms:
        try:
            result = benchmark_algorithm(algorithm, data)
            results.append(result)
            console.print(
                f"[bold green]{algorithm}[/bold green] completed in [bold]{format_time(result['time'])}[/bold]"
            )
        except Exception as e:
            console.print(
                f"[bold red]Error:[/bold red] Failed to benchmark {algorithm}: {str(e)}"
            )

    return results


def display_comparison_table(results: List[Dict[str, Any]]) -> None:
    """
    Display a comparison table of all benchmarked algorithms

    Args:
        results: List of benchmark results
    """
    if not results:
        console.print("[yellow]No results to display[/yellow]")
        return

    # Sort results by execution time
    sorted_results = sorted(results, key=lambda x: x["time"])

    # Calculate statistics
    times = [r["time"] for r in results]
    avg_time = statistics.mean(times)
    median_time = statistics.median(times)

    # Create and display the table
    table = Table(title="Sorting Algorithm Comparison")

    table.add_column("Algorithm", style="cyan")
    table.add_column("Time", style="green")
    table.add_column("Relative Performance", style="yellow")

    # Add rows for each algorithm
    for i, result in enumerate(sorted_results):
        # First algorithm is the fastest
        if i == 0:
            performance = "Fastest 🥇"
            style = "bold green"
        # Last algorithm is the slowest
        elif i == len(sorted_results) - 1:
            performance = "Slowest 🐢"
            style = "bold red"
        else:
            # Calculate how many times slower than the fastest
            ratio = result["time"] / sorted_results[0]["time"]
            performance = f"{ratio:.2f}x slower"
            style = "white"

        table.add_row(
            result["algorithm"], format_time(result["time"]), performance, style=style
        )

    # Add summary statistics
    table.add_section()
    table.add_row("Average Time", format_time(avg_time), "", style="blue")
    table.add_row("Median Time", format_time(median_time), "", style="blue")

    console.print(table)


def verify_sorting(results: List[Dict[str, Any]]) -> None:
    """
    Verify that all algorithms produced the same sorted output

    Args:
        results: List of benchmark results
    """
    if len(results) < 2:
        return

    reference = results[0]["sorted_data"]

    for result in results[1:]:
        if result["sorted_data"] != reference:
            console.print(
                f"[bold red]Warning:[/bold red] {result['algorithm']} produced different results than {results[0]['algorithm']}"
            )


def main() -> None:
    """
    Main function to run the benchmark program
    """
    parser = argparse.ArgumentParser(
        description="Benchmark sorting algorithms on text files"
    )
    parser.add_argument("file", help="Text file to sort")
    parser.add_argument(
        "-a", "--algorithm", help="Specific algorithm to benchmark (default: all)"
    )
    parser.add_argument(
        "-o", "--output", help="Save sorted output to file", action="store_true"
    )
    args = parser.parse_args()

    # Get available algorithms
    available_algorithms = get_available_algorithms()

    if not available_algorithms:
        console.print(
            "[bold red]Error:[/bold red] No sorting algorithms found in the 'sorting' directory."
        )
        sys.exit(1)

    # Validate algorithm if specified
    if args.algorithm and args.algorithm not in available_algorithms:
        console.print(
            f"[bold red]Error:[/bold red] Unknown algorithm: {args.algorithm}"
        )
        console.print(f"Available algorithms: {', '.join(available_algorithms)}")
        sys.exit(1)

    # Read input file
    console.print(f"[bold]Reading file:[/bold] {args.file}")
    data = read_file(args.file)
    console.print(f"Read [bold]{len(data)}[/bold] lines from file.")

    # Run benchmarks
    console.print("\n[bold]Starting benchmarks...[/bold]\n")

    if args.algorithm:
        # Benchmark a single algorithm
        algorithms = [args.algorithm]
    else:
        # Benchmark all available algorithms
        algorithms = available_algorithms

    results = run_all_benchmarks(data, algorithms)

    # Verify that all algorithms produced the same sorted output
    verify_sorting(results)

    # Save output if requested
    if args.output and results:
        input_filename = os.path.basename(args.file)
        if args.algorithm:
            # Save output for single algorithm
            output_filename = f"{args.algorithm}_{input_filename}"
            write_file(output_filename, results[0]["sorted_data"])
        else:
            # Save output from the fastest algorithm
            fastest = min(results, key=lambda x: x["time"])
            output_filename = f"fastest_{input_filename}"
            write_file(output_filename, fastest["sorted_data"])

    # Display comparison table for multiple algorithms
    if len(algorithms) > 1:
        console.print("\n[bold]Performance Comparison:[/bold]")
        display_comparison_table(results)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red]Benchmark interrupted by user.[/bold red]")
        sys.exit(1)
    except Exception as e:
        console.print(f"\n[bold red]Unexpected error:[/bold red] {str(e)}")
        sys.exit(1)
