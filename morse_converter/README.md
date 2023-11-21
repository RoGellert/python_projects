## Morse converter

The main idea is to have a python cli script to convert basic txt file 
with text into txt file with morse code and vice versa.

Morse representation is implemented accordingly to https://en.wikipedia.org/wiki/Morse_code

In the morse code representation, every ```\n``` (i.e end of line) signifies the end of a word.
All non-numeric characters will be cast to uppercase before conversion due to the nature of morse code.
Characters not in the morse table will be substituted by an empty string (i.e deleted).
```EOS``` signifies the end of a sentence.

In case of conversion from morse code to text, to have a meaningful input, 
the input data should be in a format of one word per line (see examples)

### Usage

To use put the file you want to convert into the same folder with script files 
and run the following command from that folder (provided python is installed)

```
py morse_converter [type_of_conversion] [name_of_the_input_file] [name_of_the_output_file]
```

for example the following command:

```
py morse_converter.py to_morse test_input_words test_output_morse
```
will convert text from ```test_input_words.txt``` to morse code,
and save in to ```test_output_morse.txt``` (newly created)

There are 2 types of conversion and 2 corresponding arguments:

- to_morse: from text to morse
- to_alphabet: from morse to text



### Examples of conversion 

File with following text:

```txt
This is
a
test
input into converter 12345.
```
will be converted into

```txt
- **** ** *** 
** *** 
*- 
- * *** - 
** -* *--* **- - 
** -* - --- 
-*-* --- -* ***- * *-* - * *-* 
*---- **--- ***-- ****- ***** EOS 
```
And the file with the following morse code:

```txt
- **** ** *** 
** *** 
*- -* 
* -**- *- -- *--* *-** * 
--- **-* 
*** --- -- * 
-- --- *-* *** * 
-*-* --- -** * 
- --- 
-*-* --- -* ***- * *-* - 
*---- **--- **--- ****- ----* ---** **--- ----* ****- ---** **--- ----* ****- EOS 
```
will be converted into

```txt
THIS
IS
AN
EXAMPLE
OF
SOME
MORSE
CODE
TO
CONVERT
1224982948294.
```