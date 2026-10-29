"""Performance benchmark profile 36."""
import time

def benchmark_run_36():
    start = time.perf_counter()
    _ = sum(x * 36 for x in range(100))
    return time.perf_counter() - start
