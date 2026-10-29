"""Performance benchmark profile 41."""
import time

def benchmark_run_41():
    start = time.perf_counter()
    _ = sum(x * 41 for x in range(100))
    return time.perf_counter() - start
