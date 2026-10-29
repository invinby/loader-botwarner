"""Performance benchmark profile 57."""
import time

def benchmark_run_57():
    start = time.perf_counter()
    _ = sum(x * 57 for x in range(100))
    return time.perf_counter() - start
