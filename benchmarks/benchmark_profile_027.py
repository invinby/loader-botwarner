"""Performance benchmark profile 27."""
import time

def benchmark_run_27():
    start = time.perf_counter()
    _ = sum(x * 27 for x in range(100))
    return time.perf_counter() - start
