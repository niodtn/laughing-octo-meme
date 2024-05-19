from pathlib import Path


class txt:
    def __init__(self, path: Path = None, read: bool = True):
        if path != None and read == True:
            self.list = self.read(path)

        self.path = path

    def __del__(self):
        if hasattr(self, "list"):
            self.write(self.path, self.list)


    def read(self, path: Path):
        with open(path, "r", encoding="utf-8") as f:
            ret = f.read().splitlines()
            ret = list(set(ret)) # Remove Duplicates
            ret.sort()

            if "" in ret: # Remove Whitespace
                ret.remove("")

            return ret

    def write(self, path: Path, _list: list[str]) -> None:
        w = ""
        for i in _list:
            w += i + "\n"

        with open(path, "w", encoding="utf-8") as f:
            f.write(w)