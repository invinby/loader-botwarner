"""Performance benchmark profile 52."""
import time

def benchmark_run_52():
    start = time.perf_counter()
    _ = sum(x * 52 for x in range(100))
    return time.perf_counter() - start
