"""Performance benchmark profile 70."""
import time

def benchmark_run_70():
    start = time.perf_counter()
    _ = sum(x * 70 for x in range(100))
    return time.perf_counter() - start
