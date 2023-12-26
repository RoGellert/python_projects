import sys


letterToMorseDict = {
    "A": "*-",
    "B": "-***",
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
    "P": "*--*",
    "Q": "--*-",
    "R": "*-*",
    "S": "***",
    "T": "-",
    "U": "**-",
    "V": "***-",
    "W": "*--",
    "X": "-**-",
    "Y": "-*--",
    "Z": "--**",
    "1": "*----",
    "2": "**---",
    "3": "***--",
    "4": "****-",
    "5": "*****",
    "6": "-****",
    "7": "--***",
    "8": "---**",
    "9": "----*",
    "0": "-----",
    ".": "EOS"
}


morseToLetterDict = {
    "*-": "A",
    "-***": "B",
    "-*-*": "C",
    "-**": "D",
    "*": "E",
    "**-*": "F",
    "--*": "G",
    "****": "H",
    "**": "I",
    "*---": "J",
    "-*-": "K",
    "*-**": "L",
    "--": "M",
    "-*": "N",
    "---": "O",
    "*--*": "P",
    "--*-": "Q",
    "*-*": "R",
    "***": "S",
    "-": "T",
    "**-": "U",
    "***-": "V",
    "*--": "W",
    "-**-": "X",
    "-*--": "Y",
    "--**": "Z",
    "*----": "1",
    "**---": "2",
    "***--": "3",
    "****-": "4",
    "*****": "5",
    "-****": "6",
    "--***": "7",
    "---**": "8",
    "----*": "9",
    "-----": "0",
    "EOS": "."
}


def return_morse_code(letter: str) -> str:
    """
    Function returning morse code corresponding to a given letter
    """
    if letter not in letterToMorseDict.keys():
        raise Exception("Invalid symbol")

    return letterToMorseDict[letter]


def return_letter(morse_code: str) -> str:
    """
    Function returning letter corresponding to a given morse code
    """
    if morse_code not in morseToLetterDict.keys():
        raise Exception("Invalid symbol")

    return morseToLetterDict[morse_code]


if __name__ == "__main__":
    if str(sys.argv[1]) in morseToLetterDict:
        print(return_letter(str(sys.argv[1])))
    elif str(sys.argv[1]) in letterToMorseDict.keys():
        print(return_morse_code(str(sys.argv[1])))
    else:
        print("Invalid argument")
