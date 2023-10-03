#!/usr/bin/python3

def add_integer(a, b=98):
    try:
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        elif not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")
        else:
            result = int(a) + int(b)
            return result
    except TypeError as e:
            return str(e)


if __name__ == "__main__":
    print("do not run script directly")
