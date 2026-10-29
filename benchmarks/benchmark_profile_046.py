"""Performance benchmark profile 46."""
import time

def benchmark_run_46():
    start = time.perf_counter()
    _ = sum(x * 46 for x in range(100))
    return time.perf_counter() - start
