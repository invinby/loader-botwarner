"""Performance benchmark profile 7."""
import time

def benchmark_run_7():
    start = time.perf_counter()
    _ = sum(x * 7 for x in range(100))
    return time.perf_counter() - start
