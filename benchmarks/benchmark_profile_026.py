"""Performance benchmark profile 26."""
import time

def benchmark_run_26():
    start = time.perf_counter()
    _ = sum(x * 26 for x in range(100))
    return time.perf_counter() - start
