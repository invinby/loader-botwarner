"""Performance benchmark profile 55."""
import time

def benchmark_run_55():
    start = time.perf_counter()
    _ = sum(x * 55 for x in range(100))
    return time.perf_counter() - start
