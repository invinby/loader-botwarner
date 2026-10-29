"""Performance benchmark profile 51."""
import time

def benchmark_run_51():
    start = time.perf_counter()
    _ = sum(x * 51 for x in range(100))
    return time.perf_counter() - start
