import os

from lib.path import *


def main():
    with open(TOKI / "number.txt", "r", encoding="utf-8") as f:
        number = f.read()
        newtoki(number)
        manatoki(number)


def newtoki(number):
    path = TOKI/"newtoki"
    url = f"newtoki{number}.com"

    txt_list = os.listdir(path)

    manga = dict()
    for txt in txt_list:
        with open(path/txt, "r", encoding="utf-8") as f:
            key = txt.split(".")[0]
            manga[key] = f.read().splitlines()

        with open(path/txt, "w", encoding="utf-8") as f:
            key = txt.split(".")[0]
            manga[key].sort()
            f.writelines(line+"\n" for line in manga[key])

    with open(FILTERS/"newtoki.txt", "w", encoding="utf-8") as f:
        f.writelines(url+"##.comment-box\n")
        f.writelines(url+"###viewcomment\n")

        for key in manga.keys():
            for name in manga[key]:
                f.writelines(
                    url+f'###webtoon-list-all > li[date-title="{name}"]\n')


def manatoki(number):
    with open(FILTERS / "manatoki.txt", "w", encoding="utf-8") as f:
        f.writelines(f"manatoki{number}.net##.comment-box\n")
        f.writelines(f"manatoki{number}.net###viewcomment\n")
