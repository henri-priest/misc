import sys
import re

def addMinutes(time, offset):

    # Enforce the time stamp pattern on the time argument
    if not re.match(r"^[0-9]{1,2}:[0-9]{2} [A,P]M$", time):
        print("Enter time in format [H]H:MM {AM|PM}")
        exit(1)

    # Enforce that offset is an integer
    offset = int(offset)

    print("Arg 1:" + time + " Type: " + str(type(time)))
    print("Arg 2:" + str(offset) + " Type: " + str(type(offset)))

if __name__ == "__main__":

    n = len(sys.argv)

    if n != 3:
        print("Requires 2 arguments")
        exit(1)

    time = sys.argv[1]
    offset = sys.argv[2]

    addMinutes(time, offset)
