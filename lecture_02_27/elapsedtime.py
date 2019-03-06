import time


class ElapsedTime:
    def __init__(self, name) -> None:
        self._name = name

    def __enter__(self):
        self._start = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self._start
        print(f"Timer {self._name}: {elapsed * 1000}ms")
