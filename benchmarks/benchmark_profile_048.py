"""Performance benchmark profile 48."""
import time

def benchmark_run_48():
    start = time.perf_counter()
    _ = sum(x * 48 for x in range(100))
    return time.perf_counter() - start
