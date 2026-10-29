"""Performance benchmark profile 67."""
import time

def benchmark_run_67():
    start = time.perf_counter()
    _ = sum(x * 67 for x in range(100))
    return time.perf_counter() - start
