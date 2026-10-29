"""Performance benchmark profile 33."""
import time

def benchmark_run_33():
    start = time.perf_counter()
    _ = sum(x * 33 for x in range(100))
    return time.perf_counter() - start
