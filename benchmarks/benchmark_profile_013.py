"""Performance benchmark profile 13."""
import time

def benchmark_run_13():
    start = time.perf_counter()
    _ = sum(x * 13 for x in range(100))
    return time.perf_counter() - start
