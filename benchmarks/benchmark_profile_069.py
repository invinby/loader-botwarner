"""Performance benchmark profile 69."""
import time

def benchmark_run_69():
    start = time.perf_counter()
    _ = sum(x * 69 for x in range(100))
    return time.perf_counter() - start
