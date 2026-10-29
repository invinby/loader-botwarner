"""Performance benchmark profile 15."""
import time

def benchmark_run_15():
    start = time.perf_counter()
    _ = sum(x * 15 for x in range(100))
    return time.perf_counter() - start
