"""Performance benchmark profile 14."""
import time

def benchmark_run_14():
    start = time.perf_counter()
    _ = sum(x * 14 for x in range(100))
    return time.perf_counter() - start
