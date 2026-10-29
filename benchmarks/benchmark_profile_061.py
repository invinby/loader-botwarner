"""Performance benchmark profile 61."""
import time

def benchmark_run_61():
    start = time.perf_counter()
    _ = sum(x * 61 for x in range(100))
    return time.perf_counter() - start
