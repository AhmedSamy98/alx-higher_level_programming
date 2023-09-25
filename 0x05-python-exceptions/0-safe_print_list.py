#!/usr/bin/python3
if __name__ == "__main__":
    # this is for the main check
    print()


def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        length = 0
        j = 0
        for j in my_list:
            length += 1

        while (i < x and i < length):
            print(f"{my_list[i]}", end="")
            i += 1
        print("")
        return i
    except IndexError:
        pass
