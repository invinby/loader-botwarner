"""Performance benchmark profile 66."""
import time

def benchmark_run_66():
    start = time.perf_counter()
    _ = sum(x * 66 for x in range(100))
    return time.perf_counter() - start
