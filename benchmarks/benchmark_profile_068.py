"""Performance benchmark profile 68."""
import time

def benchmark_run_68():
    start = time.perf_counter()
    _ = sum(x * 68 for x in range(100))
    return time.perf_counter() - start
