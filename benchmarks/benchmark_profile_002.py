"""Performance benchmark profile 2."""
import time

def benchmark_run_2():
    start = time.perf_counter()
    _ = sum(x * 2 for x in range(100))
    return time.perf_counter() - start
