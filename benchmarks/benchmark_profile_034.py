"""Performance benchmark profile 34."""
import time

def benchmark_run_34():
    start = time.perf_counter()
    _ = sum(x * 34 for x in range(100))
    return time.perf_counter() - start
