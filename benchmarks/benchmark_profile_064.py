"""Performance benchmark profile 64."""
import time

def benchmark_run_64():
    start = time.perf_counter()
    _ = sum(x * 64 for x in range(100))
    return time.perf_counter() - start
