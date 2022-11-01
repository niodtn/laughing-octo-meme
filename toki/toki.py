from lib.path import *


def main():
    with open(TOKI / "number.txt", "r", encoding="utf-8") as f:
        number =  f.read()
        newtoki(number)
        manatoki(number)

def newtoki(number):
    with open(FILTERS / "newtoki.txt", "w", encoding="utf-8") as f:
        f.writelines(f"newtoki{number}.com##.comment-box\n")
        f.writelines(f"newtoki{number}.com###viewcomment\n")

def manatoki(number):
    with open(FILTERS / "manatoki.txt", "w", encoding="utf-8") as f:
        f.writelines(f"manatoki{number}.net##.comment-box\n")
        f.writelines(f"manatoki{number}.net###viewcomment\n")
