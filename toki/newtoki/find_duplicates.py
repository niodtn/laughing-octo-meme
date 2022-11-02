import os
from pathlib import Path

PATH = Path(__file__).parent
txt_list = os.listdir(PATH)

manga = dict()
for txt in txt_list:
    file_name = txt.split(".")
    key = file_name[0]

    if file_name[1] != "txt":
        continue

    with open(PATH/txt, "r", encoding="utf-8") as f:
        manga[key] = f.read().splitlines()

    with open(PATH/txt, "w", encoding="utf-8") as f:
        manga[key].sort()
        f.writelines(line+"\n" for line in manga[key])


find = dict()
for key in manga.keys():
    for m in manga[key]:
        if not m in find:
            find[m] = list()
        find[m].append(key)

for key in find.keys():
    if len(find[key]) > 1:
        print(find[key])