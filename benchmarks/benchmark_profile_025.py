"""Performance benchmark profile 25."""
import time

def benchmark_run_25():
    start = time.perf_counter()
    _ = sum(x * 25 for x in range(100))
    return time.perf_counter() - start
