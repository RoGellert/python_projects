import sys


morseDict = {
        "A": "*-",
        "B": "*---",
        "C": "-*-*",
        "D": "-**",
        "E": "*",
        "F": "**-*",
        "G": "--*",
        "H": "****",
        "I": "**",
        "J": "*---",
        "K": "-*-",
        "L": "*-**",
        "M": "--",
        "N": "-*",
        "O": "---",
        "P": "*--*"
    }


def return_letter(letter: str) -> str:
    if letter not in morseDict.keys():
        raise Exception("Invalid symbol")

    return morseDict[letter]


if __name__ == "__main__":
    print(return_letter(str(sys.argv[1])))
