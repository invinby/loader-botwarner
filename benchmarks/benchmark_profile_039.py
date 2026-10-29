"""Performance benchmark profile 39."""
import time

def benchmark_run_39():
    start = time.perf_counter()
    _ = sum(x * 39 for x in range(100))
    return time.perf_counter() - start
