import os
import lib
from lib import toki
from lib import path


def makeUserRules():
    TXT_LIST = os.listdir(path.FILTER)
    toki.run()
    userrule = open(path.BASE / "User Rules.txt", "w", encoding="utf-8")
    for txt in TXT_LIST:
        with open(path.FILTER / txt, "r", encoding="utf-8") as f:
            userrule.write(f.read())
    userrule.close()


makeUserRules()
