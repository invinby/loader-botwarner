"""Performance benchmark profile 30."""
import time

def benchmark_run_30():
    start = time.perf_counter()
    _ = sum(x * 30 for x in range(100))
    return time.perf_counter() - start
