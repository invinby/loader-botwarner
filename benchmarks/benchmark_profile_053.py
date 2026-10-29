"""Performance benchmark profile 53."""
import time

def benchmark_run_53():
    start = time.perf_counter()
    _ = sum(x * 53 for x in range(100))
    return time.perf_counter() - start
