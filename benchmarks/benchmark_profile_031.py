"""Performance benchmark profile 31."""
import time

def benchmark_run_31():
    start = time.perf_counter()
    _ = sum(x * 31 for x in range(100))
    return time.perf_counter() - start
