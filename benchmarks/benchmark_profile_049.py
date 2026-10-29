"""Performance benchmark profile 49."""
import time

def benchmark_run_49():
    start = time.perf_counter()
    _ = sum(x * 49 for x in range(100))
    return time.perf_counter() - start
