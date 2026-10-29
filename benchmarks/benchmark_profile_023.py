"""Performance benchmark profile 23."""
import time

def benchmark_run_23():
    start = time.perf_counter()
    _ = sum(x * 23 for x in range(100))
    return time.perf_counter() - start
