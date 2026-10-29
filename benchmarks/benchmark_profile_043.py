"""Performance benchmark profile 43."""
import time

def benchmark_run_43():
    start = time.perf_counter()
    _ = sum(x * 43 for x in range(100))
    return time.perf_counter() - start
