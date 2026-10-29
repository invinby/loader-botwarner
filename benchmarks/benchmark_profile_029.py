"""Performance benchmark profile 29."""
import time

def benchmark_run_29():
    start = time.perf_counter()
    _ = sum(x * 29 for x in range(100))
    return time.perf_counter() - start
