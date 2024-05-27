import os

from lib import path
from lib.txt import txt


def booktoki(number: int) -> None:
    PATH = path.BOOKTOKI
    FILTER = path.FILTER
    URL = f"booktoki{number}.com"
    TXT_LIST = os.listdir(PATH)

    with open(FILTER / "booktoki.txt", "w", encoding="utf-8") as f:  # INITIALIZE
        # f.writelines(URL+"###viewcomment\n")  # 댓글
        # f.writelines(URL+"##.comment-box\n")  # 댓글 입력창
        f.writelines(URL + "##.sticky-wrapper > header > div > *\n")  # 로고

    _booktoki = open(FILTER / "booktoki.txt", "a", encoding="utf-8")

    for txt_name in TXT_LIST:
        _txt = txt(PATH / txt_name)
        data = _txt.list.copy()

        for i in range(len(data)):
            selecter = f'###webtoon-list-all > li[date-title="{data[i]}"]\n'
            data[i] = URL + selecter

        for i in data:
            _booktoki.writelines(i)

    _booktoki.close()
