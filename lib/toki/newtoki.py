import os

from lib import path
from lib.txt import txt


def newtoki(number: int) -> None:
    PATH = path.NEWTOKI
    FILTER = path.FILTER
    URL = f"newtoki{number}.com"
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
