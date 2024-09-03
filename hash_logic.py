iso_hashmap = {
    "a": "4",
    "b": "8",
    "c": "(",
    "d": "|)",
    "e": "3",
    # "f": "",
    "g": "6",
    "h": "#",
    "i": "!",
    # "j": "",
    "k": "|{",
    "L": "L",
    # "m": "",
    "n": "π",
    "o": "0",
    "p": "9",
    # "q": "",
    "r": "₹",
    "s": "5",
    "t": "7",
    # "u": "",
    "v": "^",
    "w": "^^",
    "x": "}{",
    "y": "¥",
    # "z": ""
}


def iscii_hash(string: str) -> str:
    string_list = [i for i in string.lower()]
    for index, char in enumerate(string_list):
        if char in iso_hashmap:
            string_list.pop(index)
            string_list.insert(index, iso_hashmap[char])

    return "".join(string_list)
