"""Performance benchmark profile 37."""
import time

def benchmark_run_37():
    start = time.perf_counter()
    _ = sum(x * 37 for x in range(100))
    return time.perf_counter() - start
