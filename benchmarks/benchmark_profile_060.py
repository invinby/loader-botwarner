"""Performance benchmark profile 60."""
import time

def benchmark_run_60():
    start = time.perf_counter()
    _ = sum(x * 60 for x in range(100))
    return time.perf_counter() - start
