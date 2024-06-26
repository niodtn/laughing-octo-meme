from lib import path
import os
from lib.txt import txt


def find(p):
    FILE_LIST = os.listdir(p)
    dups = dict()

    # txt를 전부 읽어서 아래처럼 만듬
    # {"웹툰 제목": ["1.txt", "2.txt"], ...}
    for file in FILE_LIST:
        _txt = txt(p / file)

        for title in _txt.list:
            if not title in dups:
                dups[title] = list()
            dups[title].append(file)

    # 웹툰 제목이 하나의 파일 안에 있지 않을 때
    for key in dups.keys():
        if len(dups[key]) != 1:
            print(key)
            print(dups[key])

            user_input = input("Ban? (y/N): ")
            if user_input.lower() in ["yes", "y"]:
                for i in dups[key]:
                    _txt = txt(p / i)
                    _txt.list.remove(key)

                _txt = txt(p / "Ban.txt")
                _txt.list.append(key + "\n")


print("뉴토끼")
find(path.NEWTOKI)
print("북토끼")
find(path.BOOKTOKI)
