"""Performance benchmark profile 28."""
import time

def benchmark_run_28():
    start = time.perf_counter()
    _ = sum(x * 28 for x in range(100))
    return time.perf_counter() - start
