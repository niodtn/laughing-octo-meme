import lib
from lib import path
import os

FILE_LIST = os.listdir(path.NEWTOKI)

dups = dict()
for file in FILE_LIST:
    with open(path.NEWTOKI/file, "r", encoding="utf-8") as f:
        title_list = lib.sort(f.read())

    for title in title_list:
        if not title in dups:
            dups[title] = list()
        dups[title].append(file)

for key in dups.keys():
    if len(dups[key]) != 1:
        print(key)
        print(dups[key])