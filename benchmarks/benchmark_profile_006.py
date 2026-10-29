"""Performance benchmark profile 6."""
import time

def benchmark_run_6():
    start = time.perf_counter()
    _ = sum(x * 6 for x in range(100))
    return time.perf_counter() - start
