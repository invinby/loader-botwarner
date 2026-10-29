"""Performance benchmark profile 62."""
import time

def benchmark_run_62():
    start = time.perf_counter()
    _ = sum(x * 62 for x in range(100))
    return time.perf_counter() - start
