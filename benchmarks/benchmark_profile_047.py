"""Performance benchmark profile 47."""
import time

def benchmark_run_47():
    start = time.perf_counter()
    _ = sum(x * 47 for x in range(100))
    return time.perf_counter() - start
