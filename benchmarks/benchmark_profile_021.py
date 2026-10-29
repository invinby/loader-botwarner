"""Performance benchmark profile 21."""
import time

def benchmark_run_21():
    start = time.perf_counter()
    _ = sum(x * 21 for x in range(100))
    return time.perf_counter() - start
