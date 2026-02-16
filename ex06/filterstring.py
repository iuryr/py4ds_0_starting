import sys
from ft_filter import ft_filter


def capture_inputs(args: list[str]) -> tuple[str, int]:
    """
    Parse inputs necessary to the program. Raises exception if anything bad
    happens.
    """
    if len(args) != 3:
        raise AssertionError("the arguments are bad")

    text = args[1]

    try:
        size = int(args[2])
    except Exception:
        raise AssertionError("the arguments are bad")

    return text, size


def main():
    """
    Program entrypoint.
    """
    try:
        text, size = capture_inputs(sys.argv)
        big_words = [word for word in
                     ft_filter(lambda x: len(x) > size, text.split(" "))]
        print(big_words)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    return


if __name__ == "__main__":
    main()
