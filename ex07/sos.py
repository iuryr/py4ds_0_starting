import sys

NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def capture_input(args: list[str]) -> str:
    """Capture input if proper. Raise exception otherwise"""
    if len(args) != 2:
        raise AssertionError("the arguments are bad")
    for c in args[1]:
        if c.isalnum() is False and c.isspace() is False:
            raise AssertionError("the arguments are bad")
    return args[1].upper()


def main():
    """Program entrypoint"""
    try:
        text = capture_input(sys.argv)
        trans_table = str.maketrans(NESTED_MORSE)
        morse_code = text.translate(trans_table)
        print(morse_code)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    return


if __name__ == "__main__":
    main()
