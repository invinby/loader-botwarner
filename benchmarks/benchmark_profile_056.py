"""Performance benchmark profile 56."""
import time

def benchmark_run_56():
    start = time.perf_counter()
    _ = sum(x * 56 for x in range(100))
    return time.perf_counter() - start
