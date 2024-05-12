from lib import path
from lib.toki.booktoki import booktoki
from lib.toki.manatoki import manatoki
from lib.toki.newtoki import newtoki


def run():
    with open(path.DATA / "toki" / "number.txt", "r", encoding="utf-8") as f:
        number = int(f.read())
        booktoki(number)
        # manatoki(number)
        newtoki(number)
