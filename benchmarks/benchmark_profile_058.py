"""Performance benchmark profile 58."""
import time

def benchmark_run_58():
    start = time.perf_counter()
    _ = sum(x * 58 for x in range(100))
    return time.perf_counter() - start
