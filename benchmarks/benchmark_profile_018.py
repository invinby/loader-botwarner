"""Performance benchmark profile 18."""
import time

def benchmark_run_18():
    start = time.perf_counter()
    _ = sum(x * 18 for x in range(100))
    return time.perf_counter() - start
