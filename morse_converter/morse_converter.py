from morse_dicts import letterToMorseDict, morseToLetterDict
import sys


def convert(argv: list[str]):
    if not len(argv) == 4:
        raise Exception("Invalid argument num")

    if argv[1] not in ["from_morse", "to_morse"]:
        raise Exception("Invalid operation type argument\n " +
                        "Accepted arguments: [from_morse, to_morse]")

    return


def preprocess_string(text: list[str]) -> list[list[str]]:
    text_processed = []
    for i in range(len(text)):
        text_processed.append(text[i].strip().split(" "))

    return text_processed


if __name__ == "__main__":
    with open("test_input_morse.txt") as f:
        lines = f.readlines()
    print(lines)
    print(preprocess_string(lines))
    f.close()


