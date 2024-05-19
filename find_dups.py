import lib
from lib import path
import os

FILE_LIST = os.listdir(path.NEWTOKI)
"""data/newtoki 폴더의 txt 파일 이름 리스트"""

dups = dict()

# txt를 전부 읽어서 아래처럼 만듬
# {"웹툰 제목": ["1.txt", "2.txt"], ...}
for file in FILE_LIST:
    with open(path.NEWTOKI/file, "r", encoding="utf-8") as f:
        title_list = lib.sort(f.read())

    for title in title_list:
        if not title in dups:
            dups[title] = list()
        dups[title].append(file)

# 웹툰 제목이 하나의 파일 안에 있지 않을 때
for key in dups.keys():
    if len(dups[key]) != 1:
        print(key)
        print(dups[key])
        for txt in dups[key]:
            if txt is 'Ban.txt':
                continue
            with open(path.NEWTOKI/txt, "r", encoding="utf-8") as f:
                data = lib.sort(f.read())
            data.remove(key)
            with open(path.NEWTOKI/txt, "w", encoding="utf-8") as f:
                f.write(lib.list_str(data))
