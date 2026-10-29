"""Performance benchmark profile 24."""
import time

def benchmark_run_24():
    start = time.perf_counter()
    _ = sum(x * 24 for x in range(100))
    return time.perf_counter() - start
