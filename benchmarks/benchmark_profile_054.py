"""Performance benchmark profile 54."""
import time

def benchmark_run_54():
    start = time.perf_counter()
    _ = sum(x * 54 for x in range(100))
    return time.perf_counter() - start
