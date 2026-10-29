"""Performance benchmark profile 40."""
import time

def benchmark_run_40():
    start = time.perf_counter()
    _ = sum(x * 40 for x in range(100))
    return time.perf_counter() - start
