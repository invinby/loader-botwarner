"""Performance benchmark profile 38."""
import time

def benchmark_run_38():
    start = time.perf_counter()
    _ = sum(x * 38 for x in range(100))
    return time.perf_counter() - start
