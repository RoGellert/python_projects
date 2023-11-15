from morse_dicts import letterToMorseDict, morseToLetterDict
import sys


def convert(argv: list[str]):
    if not len(argv) == 4:
        raise Exception("Invalid argument num")

    if argv[1] not in ["from_morse", "to_morse"]:
        raise Exception("Invalid operation type argument\n " +
                        "Accepted arguments: [from_morse, to_morse]")

    return


def preprocess_string(text: list[str]) -> list[str]:
    if text[len(text)-1] == "":
        for i in range(len(text)-1):
            text[i] = text[i][:-1]
    else:
        for i in range(len(text)):
            text[i] = text[i][:-1]

    return text


if __name__ == "__main__":
    with open("test_input1.txt") as f:
        lines = f.readlines()
    #convert(sys.argv)
    print(lines)
    print(preprocess_string(lines))
    f.close()

