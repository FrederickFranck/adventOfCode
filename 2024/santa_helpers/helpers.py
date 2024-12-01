from pathlib import Path
import inspect


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
