"""Performance benchmark profile 42."""
import time

def benchmark_run_42():
    start = time.perf_counter()
    _ = sum(x * 42 for x in range(100))
    return time.perf_counter() - start
