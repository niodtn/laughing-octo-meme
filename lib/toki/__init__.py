from lib import path
from lib.toki.booktoki import booktoki
from lib.toki.newtoki import newtoki
from lib.toki.toki import toki


def run():
    with open(path.DATA / "toki" / "number.txt", "r", encoding="utf-8") as f:
        number = int(f.read())
        toki("new", number)
        toki("book", number)
