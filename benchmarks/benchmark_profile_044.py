"""Performance benchmark profile 44."""
import time

def benchmark_run_44():
    start = time.perf_counter()
    _ = sum(x * 44 for x in range(100))
    return time.perf_counter() - start
