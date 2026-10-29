"""Performance benchmark profile 10."""
import time

def benchmark_run_10():
    start = time.perf_counter()
    _ = sum(x * 10 for x in range(100))
    return time.perf_counter() - start
