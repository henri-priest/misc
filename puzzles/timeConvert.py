import sys
import re

def timeCovert(time, offset):
    print("Arg 1:" + arg1 + " Type: " + str(type(arg1)))
    print("Arg 2:" + arg2 + " Type: " + str(type(arg2)))

if __name__ == "__main__":

    n = len(sys.argv)

    if n != 3:
        print("Requires 2 arguments")
        exit(1)

    arg1 = sys.argv[1]
    arg2 = sys.argv[2]

    if re.match(r"[0-9]{1,2}:[0-9]{2} +", arg1):
        print("Matches regex")
    else:
        print("Does not match regex")

    timeCovert(arg1, arg2)
