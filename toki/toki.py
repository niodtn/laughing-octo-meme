import os
from pathlib import Path

TOKI = Path(__file__).parent
FILTERS = TOKI.parent / "filters"


def main():
    with open(TOKI / "number.txt", "r", encoding="utf-8") as f:
        number = f.read().splitlines()[0]
        newtoki(number)
        manatoki(number)


def newtoki(number):
    PATH = TOKI/"newtoki"
    url = f"newtoki{number}.com"

    txt_list = os.listdir(PATH)
    manga = dict()
    for txt in txt_list:
        file_name = txt.split(".")
        # check extension
        if file_name[1] != "txt":
            continue

        with open(PATH/txt, "r", encoding="utf-8") as f:
            manga[file_name[0]] = f.read().splitlines()

        with open(PATH/txt, "w", encoding="utf-8") as f:
            manga[file_name[0]] = list(set(manga[file_name[0]]))
            manga[file_name[0]].sort()

            if "" in manga[file_name[0]]:
                manga[file_name[0]].remove("")

            f.writelines(line+"\n" for line in manga[file_name[0]])

    with open(FILTERS/"newtoki.txt", "w", encoding="utf-8") as f:
        # 댓글
        f.writelines(url+"###viewcomment\n")
        # 댓글 입력창
        f.writelines(url+"##.comment-box\n")
        # 별점
        # f.writelines(url+"###content_wrapper > div.content:last-child > div.at-content > div.view-wrap:nth-child(7) > section:nth-child(2) > article > div.view-title:first-child > div.view-content > div.row > div.col-sm-8:last-child > div.view-content:last-child > table.table > tbody:last-child > tr > th.active > button.btn.btn-white.btn-sm:nth-child(4)\n")

        for key in manga.keys():
            for name in manga[key]:
                f.writelines(
                    url+f'###webtoon-list-all > li[date-title="{name}"]\n')


def manatoki(number):
    with open(FILTERS / "manatoki.txt", "w", encoding="utf-8") as f:
        f.writelines(f"manatoki{number}.net##.comment-box\n")
        f.writelines(f"manatoki{number}.net###viewcomment\n")
