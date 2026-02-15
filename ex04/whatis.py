import sys

if len(sys.argv) == 1:
    sys.exit(0)

try:
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")

    try:
        number = int(sys.argv[1])
        message = "I'm Even." if number % 2 == 0 else "I'm Odd."
        print(message)

    except ValueError:
        raise AssertionError("argument is not an integer")

except AssertionError as e:
    print(f"{type(e).__name__}: {e}")
