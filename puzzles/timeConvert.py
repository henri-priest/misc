import sys

n = len(sys.argv)

if n != 3:
    print("Requires 2 arguments")
    exit(1)

arg1 = sys.argv[1]
arg2 = sys.argv[2]

print("Arg 1:" + arg1 + " Type: " + str(type(arg1)))
print("Arg 2:" + arg2 + " Type: " + str(type(arg2)))