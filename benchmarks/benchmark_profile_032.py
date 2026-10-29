"""Performance benchmark profile 32."""
import time

def benchmark_run_32():
    start = time.perf_counter()
    _ = sum(x * 32 for x in range(100))
    return time.perf_counter() - start
