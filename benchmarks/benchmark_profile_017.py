"""Performance benchmark profile 17."""
import time

def benchmark_run_17():
    start = time.perf_counter()
    _ = sum(x * 17 for x in range(100))
    return time.perf_counter() - start
