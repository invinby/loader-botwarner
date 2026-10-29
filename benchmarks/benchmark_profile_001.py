"""Performance benchmark profile 1."""
import time

def benchmark_run_1():
    start = time.perf_counter()
    _ = sum(x * 1 for x in range(100))
    return time.perf_counter() - start
