"""Performance benchmark profile 5."""
import time

def benchmark_run_5():
    start = time.perf_counter()
    _ = sum(x * 5 for x in range(100))
    return time.perf_counter() - start
