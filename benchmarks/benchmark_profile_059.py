"""Performance benchmark profile 59."""
import time

def benchmark_run_59():
    start = time.perf_counter()
    _ = sum(x * 59 for x in range(100))
    return time.perf_counter() - start
