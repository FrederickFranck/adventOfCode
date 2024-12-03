from pathlib import Path
import inspect
import time


def read_input(demo=True):
    caller = inspect.stack()[1].filename
    path = Path(caller.split("/solution.py")[0])
    if demo:
        filename = str(path / "test.txt")
    else:
        filename = str(path / "input.txt")

    with open(filename, "r") as file:
        content = file.read()
    return content


def _start():
    return time.perf_counter()


def _stop(start):
    print(f"took {(time.perf_counter()-start)*1000} ms")
