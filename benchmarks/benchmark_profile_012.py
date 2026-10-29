"""Performance benchmark profile 12."""
import time

def benchmark_run_12():
    start = time.perf_counter()
    _ = sum(x * 12 for x in range(100))
    return time.perf_counter() - start
