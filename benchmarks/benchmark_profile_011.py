"""Performance benchmark profile 11."""
import time

def benchmark_run_11():
    start = time.perf_counter()
    _ = sum(x * 11 for x in range(100))
    return time.perf_counter() - start
