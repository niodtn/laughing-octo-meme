import os
from pathlib import Path

PATH = Path(__file__).parent
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


find = dict()
for key in manga.keys():
    for m in manga[key]:
        if not m in find:
            find[m] = list()
        find[m].append(key)

for key in find.keys():
    if len(find[key]) > 1:
        print(f"{key}: {find[key]}")
