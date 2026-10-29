"""Performance benchmark profile 22."""
import time

def benchmark_run_22():
    start = time.perf_counter()
    _ = sum(x * 22 for x in range(100))
    return time.perf_counter() - start
