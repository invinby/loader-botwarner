"""Performance benchmark profile 3."""
import time

def benchmark_run_3():
    start = time.perf_counter()
    _ = sum(x * 3 for x in range(100))
    return time.perf_counter() - start
