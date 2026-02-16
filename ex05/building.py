from string import punctuation
import sys

def capture_input(args: list[str]) -> str:
    if len(args) == 1:
        print("What is the text to count?")
        text = sys.stdin.readline()
        return text
    if len(args) == 2:
        return args[1]
    if len(args) > 2:
        raise AssertionError("this program requires only one argument.")

def count_and_display(text: str):
    char_count = len(text)
    uppercase_count = 0
    lowercase_count = 0
    punctuation_count = 0
    space_count = 0
    digits_count = 0

    for c in text:
        if c.isupper():
            uppercase_count += 1
            continue
        if c.islower():
            lowercase_count += 1
            continue
        if c in punctuation:
            punctuation_count += 1
            continue
        if c.isspace():
            space_count += 1
            continue
        if c.isdigit():
            digits_count += 1
            continue

    print(f"The text contains {char_count} characters:")
    print(f"{uppercase_count} upper letters")
    print(f"{lowercase_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digits_count} digits")
    return


def main():
    try:
        text = capture_input(sys.argv)
        count_and_display(text)
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
