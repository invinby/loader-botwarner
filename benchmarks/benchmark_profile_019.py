"""Performance benchmark profile 19."""
import time

def benchmark_run_19():
    start = time.perf_counter()
    _ = sum(x * 19 for x in range(100))
    return time.perf_counter() - start
