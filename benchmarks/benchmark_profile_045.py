"""Performance benchmark profile 45."""
import time

def benchmark_run_45():
    start = time.perf_counter()
    _ = sum(x * 45 for x in range(100))
    return time.perf_counter() - start
