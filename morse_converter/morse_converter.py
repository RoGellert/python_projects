from morse_dicts import letterToMorseDict, morseToLetterDict
import sys


def convert(argv: list[str]):
    if not len(argv) == 4:
        raise Exception("Invalid argument num")

    if argv[1] not in ["to_alphabet", "to_morse"]:
        raise Exception("Invalid operation type argument\n " +
                        "Accepted arguments: [to_alphabet, to_morse]")

    with open(f"{argv[2]}.txt") as file_to_read:
        text = file_to_read.readlines()
    file_to_read.close()

    text_processed = preprocess_string(text)

    output_text = ""
    if argv[1] == "to_alphabet":
        output_text = convert_morse_to_text(text_processed)
    elif argv[1] == "to_morse":
        output_text = convert_text_to_morse(text_processed)

    with open(f"{argv[3]}.txt", "x") as file_to_write:
        file_to_write.write(output_text)
    file_to_write.close()

    return


def preprocess_string(text: list[str]) -> list[list[str]]:
    text_processed = [i.strip().split(" ") for i in text]

    return text_processed


def convert_text_to_morse(text: list[list[str]]) -> str:
    output_text = ""
    for i in text:
        for j in i:
            for k in j:
                if k.upper() in letterToMorseDict.keys():
                    output_text += f"{letterToMorseDict[k.upper()]} "
            output_text += "\n"

    return output_text


def convert_morse_to_text(text: list[list[str]]) -> str:
    output_text = ""
    for i in text:
        for j in i:
            if j in morseToLetterDict.keys():
                output_text += f"{morseToLetterDict[j]}"
        output_text += "\n"

    return output_text


if __name__ == "__main__":
    convert(sys.argv)


