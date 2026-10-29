"""Performance benchmark profile 50."""
import time

def benchmark_run_50():
    start = time.perf_counter()
    _ = sum(x * 50 for x in range(100))
    return time.perf_counter() - start
