import sys
import re

def addMinutes(time, offset):

    if re.match(r"^[0-9]{1,2}:[0-9]{2} [A,P]M$", time):
        print("Matches regex")
    else:
        print("Does not match regex")

    print("Arg 1:" + time + " Type: " + str(type(time)))
    print("Arg 2:" + offset + " Type: " + str(type(offset)))

if __name__ == "__main__":

    n = len(sys.argv)

    if n != 3:
        print("Requires 2 arguments")
        exit(1)

    time = sys.argv[1]
    offset = sys.argv[2]

    addMinutes(time, offset)
