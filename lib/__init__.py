def list_str(_list: list) -> str:
    ret = ""
    for i in _list:
        ret += i + "\n"
    return ret


def sort(string: str) -> list[str]:
    """
    txt같은 문자열이 담긴 파일을 `\\n`을 기준으로 리스트로 변환
    """
    _list = string.splitlines()
    _list = list(set(_list))  # 중복 제거
    _list.sort()
    if "" in _list:  # 공백 제거
        _list.remove("")
    return _list

