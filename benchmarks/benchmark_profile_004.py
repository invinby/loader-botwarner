"""Performance benchmark profile 4."""
import time

def benchmark_run_4():
    start = time.perf_counter()
    _ = sum(x * 4 for x in range(100))
    return time.perf_counter() - start
