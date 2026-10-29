"""Performance benchmark profile 8."""
import time

def benchmark_run_8():
    start = time.perf_counter()
    _ = sum(x * 8 for x in range(100))
    return time.perf_counter() - start
