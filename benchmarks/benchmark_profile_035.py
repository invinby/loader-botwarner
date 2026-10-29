"""Performance benchmark profile 35."""
import time

def benchmark_run_35():
    start = time.perf_counter()
    _ = sum(x * 35 for x in range(100))
    return time.perf_counter() - start
