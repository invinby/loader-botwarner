"""Performance benchmark profile 16."""
import time

def benchmark_run_16():
    start = time.perf_counter()
    _ = sum(x * 16 for x in range(100))
    return time.perf_counter() - start
