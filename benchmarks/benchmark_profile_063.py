"""Performance benchmark profile 63."""
import time

def benchmark_run_63():
    start = time.perf_counter()
    _ = sum(x * 63 for x in range(100))
    return time.perf_counter() - start
