#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    sum = len(sys.argv) - 1
    if sum == 0:
        print("0 arguments.")
    elif sum == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(sum))
    for i in range(sum):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
