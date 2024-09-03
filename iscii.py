iso_hashmap = {
    # ALPHABETS
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
    "l": "1",
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
    "x": "><",
    "y": "¥",
    "z": "2",
    # NUMBERS
    "1": "l",
    "2": "z",
    "3": "e",
    "4": "a",
    "5": "s",
    "6": "g",
    "7": "t",
    "8": "b",
    "9": "p",
    "0": "o",
}

inv_iso_hashmap = {v: k for k, v in iso_hashmap.items()}


def encode(string: str) -> str:
    return "".join(iso_hashmap.get(char, char) for char in string.lower())


def decode(string: str) -> str:
    decoded_string = ""
    i = 0

    while i < len(string):
        # Check for multi-character mappings
        found = False
        for length in range(3, 0, -1):  # Check for lengths 3, 2, and 1
            substring = string[i : i + length]
            if substring in inv_iso_hashmap:
                decoded_string += inv_iso_hashmap[substring]
                i += length
                found = True
                break
        if not found:
            decoded_string += string[i]
            i += 1

    return decoded_string


if __name__ == "__main__":
    original_string = "Hello chia, hitz, daddy, and the Whole Wide World."
    encoded_string = encode(original_string)
    decoded_string = decode(encoded_string)

    print("Original:", original_string)
    print("Encoded:", encoded_string)
    print("Decoded:", decoded_string)
