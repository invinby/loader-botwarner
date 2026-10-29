"""Performance benchmark profile 20."""
import time

def benchmark_run_20():
    start = time.perf_counter()
    _ = sum(x * 20 for x in range(100))
    return time.perf_counter() - start
