from morse_dicts import letterToMorseDict, morseToLetterDict
import sys


def convert(argv: list[str]):
    """
    Function to open a file, convert (text to morse and vice versa) and save in a file

    argv[1]: either [to_morse] or [to_alphabet] signifying type of conversion
    argv[2]: name of input file
    argv[3]: name of output file to create and save the result of conversion
    """
    # check the quantity of arguments
    if not len(argv) == 4:
        raise Exception("Invalid argument num")

    # check if type of conversion input is correct
    if argv[1] not in ["to_alphabet", "to_morse"]:
        raise TypeError("Invalid operation type argument\n " +
                        "Accepted arguments: [to_alphabet, to_morse]")

    # open the file to read from
    with open(f"{argv[2]}.txt") as file_to_read:
        text = file_to_read.readlines()
    file_to_read.close()

    text_processed = preprocess_string(text)

    # convert the text
    output_text = ""
    if argv[1] == "to_alphabet":
        output_text = convert_morse_to_text(text_processed)
    elif argv[1] == "to_morse":
        output_text = convert_text_to_morse(text_processed)

    # save in a file
    with open(f"{argv[3]}.txt", "x") as file_to_write:
        file_to_write.write(output_text)
    file_to_write.close()

    return


def preprocess_string(text: list[str]) -> list[list[str]]:
    """
    Function to do some processing on a string
    """
    text_processed = [i.strip().split(" ") for i in text]

    return text_processed


def convert_text_to_morse(text: list[list[str]]) -> str:
    """
    Function to parse and convert text to morse based on a dictionary
    """
    output_text = ""
    for i in text:
        for j in i:
            for k in j:
                if k.upper() in letterToMorseDict.keys():
                    output_text += f"{letterToMorseDict[k.upper()]} "
            output_text += "\n"

    return output_text


def convert_morse_to_text(text: list[list[str]]) -> str:
    """
    Function to parse and convert morse to text based on a dictionary
    """
    output_text = ""
    for i in text:
        for j in i:
            if j in morseToLetterDict.keys():
                output_text += f"{morseToLetterDict[j]}"
        output_text += "\n"

    return output_text


if __name__ == "__main__":
    convert(sys.argv)
    print(f"Created output file {sys.argv[3]}.txt")
