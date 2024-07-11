import os

from lib import path
from lib.txt import txt


def toki(toki: str, number: int) -> None:
    PATH = path.DATA / "toki" / f"{toki}toki"
    FILTER = path.FILTER

    URL = f"{toki}toki{number}."
    URL += "net" if toki == "mana" else "com"

    TXT_LIST = os.listdir(PATH)

    with open(FILTER / "newtoki.txt", "w", encoding="utf-8") as f:  # INITIALIZE
        # f.writelines(URL+"###viewcomment\n")  # 댓글
        # f.writelines(URL+"##.comment-box\n")  # 댓글 입력창
        f.writelines(URL + "##.sticky-wrapper > header > div > *\n")  # 로고

    _newtoki = open(FILTER / "newtoki.txt", "a", encoding="utf-8")

    for txt_name in TXT_LIST:
        # 확장자가 txt가 아니면 스킵
        if txt_name.split(".")[-1] != "txt":
            continue

        _txt = txt(PATH / txt_name)
        data = _txt.list.copy()

        for i in range(len(data)):
            selecter = f'###webtoon-list-all > li[date-title="{data[i]}"]\n'
            data[i] = URL + selecter

        for i in data:
            _newtoki.writelines(i)

    _newtoki.close()


# class toki:
#     PATH_FILTER = path.FILTER
#     PATH_DATA_NEW = path.DATA / "toki" / "newtoki"
#     PATH_DATA_BOOK = path.DATA / "toki" / "booktoki"
#     PATH_DATA_MANA = path.DATA / "toki" / "manatoki"

#     def __init__(self, number: int) -> None:
#         self.num = number
#         newtoki = new(path.FILTER / "newtoki.txt")
#         booktoki = book(path.FILTER / "booktoki.txt")
#         manatoki = mana(path.FILTER / "manatoki.txt")

#     @property
#     def num(self) -> int:
#         return self.toki_num

#     @num.setter
#     def num(self, number: int) -> None:
#         self.toki_num = number


# class new:
#     def __init__(self, path) -> None:
#         with open(path, "w", encoding="utf-8") as f:
#             wls = URL + "##.sticky-wrapper > header > div > *\n"
