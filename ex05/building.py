from string import punctuation
import sys


def capture_input(args: list[str]) -> str:
    """
    Capture text from argument or user input.

    Raises exception if multiple arguments are passed to command line.
    """
    if len(args) == 1:
        print("What is the text to count?")
        text = sys.stdin.readline()
        return text
    elif len(args) == 2:
        return args[1]
    else:
        raise AssertionError("this program requires only one argument.")


def count_and_display(text: str):
    """
    text (input string): The text to analyze

    Prints the following information:
    1. The number of characters in the text
    2. The number of upper case letters
    3. The number of lower case letters
    4. The number of punctuation marks
    5. The number of spaces
    6. The number of digits
    """
    char_count = len(text)

    uppercase_count = sum(c.isupper() for c in text)
    lowercase_count = sum(c.islower() for c in text)
    punctuation_count = sum(c in punctuation for c in text)
    space_count = sum(c.isspace() for c in text)
    digits_count = sum(c.isdigit() for c in text)

    print(f"The text contains {char_count} characters:")
    print(f"{uppercase_count} upper letters")
    print(f"{lowercase_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digits_count} digits")
    return


def main():
    """
    Captures text, analyze it and display it.
    Handles exception if multiple clarguments are passed.
    """
    try:
        text = capture_input(sys.argv)
        count_and_display(text)
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
