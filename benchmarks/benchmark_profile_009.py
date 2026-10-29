"""Performance benchmark profile 9."""
import time

def benchmark_run_9():
    start = time.perf_counter()
    _ = sum(x * 9 for x in range(100))
    return time.perf_counter() - start
