"""Performance benchmark profile 65."""
import time

def benchmark_run_65():
    start = time.perf_counter()
    _ = sum(x * 65 for x in range(100))
    return time.perf_counter() - start
