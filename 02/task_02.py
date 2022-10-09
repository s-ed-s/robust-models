import time


class MyTimer:
    def __init__(self, units):
        self.units = units

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.stop_time = time.perf_counter()

    def elapsed_time(self):
        self.spent_time = self.stop_time - self.start_time

        if self.units == 'm':
            self.spent_time /= 60
        elif self.units == 'h':
            self.spent_time /= 3_600
        return f"{self.spent_time:.8}"
