def list_str(_list: list) -> str:
    ret = ""
    for i in _list:
        ret += i + "\n"
    return ret


def sort(string: str) -> list[str]:
    _list = string.splitlines()
    _list = list(set(_list))  # REMOVE duplicates
    _list.sort()
    if "" in _list:  # REMOVE white spapce
        _list.remove("")
    return _list
