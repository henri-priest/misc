# For creating the random input to the assembly line
from random import randint as rand

# For allowing a console output delay for debugging/visualization of process
from time import sleep as sleep

# For allowing console call to 'cls' to clear the console window each loop
from os import system as system

# Number of times the assembly line runs
ITERATIONS = 100

# Length of assembly line
BELT_LEN = 5

# Number of pairs of workers
NUM_WORKERS = 3

# Space between each worker
WORKER_SPACE = 1

class WorkerPair(object):

    def __init__(self):
        # Each worker will be a string, with 1-3 characters.
        # Char 1 is the worker's time left to assemble finaly product.
        # Char 2 and 3 can be an A part or B part (cannot have A and B) or a finished product (P)
        self.worker1 = "3"
        self.worker2 = "3"

    def print_workers(self):
        # This method was useful for debugging and provides live feedback on cosnole
        return str("\n" + " W1=" + self.worker1 + "\n" + " W2=" + str(self.worker2))

    def make(self, worker):
         # Worker checks if they have an A and a B, and if so then checks the time left to assemple P
        if "b" in worker and "a" in worker:
            if worker[0] == str(0):
                worker = worker.replace("0", "3")
                worker = worker.replace("a", "")
                worker = worker.replace("b", "")
                worker += "p"
            else:
                count = int( worker[0] )
                count2 = count - 1
                worker = worker.replace( str(count) , str(count2) )

        return worker


    def action(self, value):

        # Put all of the logic checks into a class method so it only has to be called once in main loop

        item = value
        # e = empty tray
        # a = A type part
        # b = B type part
        # p = finished product

        if value == "e":
            # Placing finished product is highest priotity
            if "p" in self.worker1:
                self.worker1 = self.worker1.replace('p','')
                item = "p"
            elif "p" in self.worker2:
                self.worker2 = self.worker2.replace('p','')
                item = "p"

            # If worker does not have finished product they should check if they have the parts for next iteration
            self.worker1 = self.make(self.worker1)
            self.worker2 = self.make(self.worker2)

        elif value == "a":
            # Only take an A part if you don't have one already and hands are not full
            if "a" not in self.worker1 and len(self.worker1) < 3:
                self.worker1 += "a"
                self.worker2 = self.make(self.worker2)
                item = "e"
            elif "a" not in self.worker2 and len(self.worker2) < 3:
                self.worker2 += "a"
                self.worker1 = self.make(self.worker1)
                item = "e"
            else:
                self.worker1 = self.make(self.worker1)
                self.worker2 = self.make(self.worker2)

        elif value == "b":
            # Only take a B part if you don't have one already one and hands are not full
            if "b" not in self.worker1 and len(self.worker1) < 3:
                self.worker1 += "b"
                self.worker2 = self.make(self.worker2)
                item = "e"
            elif "b" not in self.worker2 and len(self.worker2) < 3:
                self.worker2 += "b"
                self.worker1 = self.make(self.worker1)
                item = "e"
            else:
                self.worker1 = self.make(self.worker1)
                self.worker2 = self.make(self.worker2)

        elif value == "p":
            # Finished item is on tray, do not take
            self.worker1 = self.make(self.worker1)
            self.worker2 = self.make(self.worker2)

        return item

# Create assembly line based on global parameter
belt = ['e'] * BELT_LEN

# Create worker pairs based on global parameter
worker_list = [WorkerPair() for pos in range(NUM_WORKERS)]

# Initialize array for showing live output
output = []

# Initialize part/empty tray counts
a_count = 0
b_count = 0
e_count = 0
p_count = 0

# Clear screen
system('cls')

# Loop for number of predefined iterations
for i in range(ITERATIONS):

    # Initial display
    print("Iteration = " + str(i))
    print("")
    print("Assembly line:")
    print(str(belt))
    print("")

    # This is where the worker pair modifies the assembly line position
    for i in range(NUM_WORKERS):
        # Workers position is based on the spacing variable
        belt[ i * WORKER_SPACE ] = worker_list[i].action(belt[i])
        print("Worker pair " + str(i) + ": " + worker_list[i].print_workers())

    # Create next item (1 of 3 types) and push on to assembly line
    next = rand(0,2)
    if next == 0:
        belt.insert(0, 'a')
    elif next == 1:
        belt.insert(0, 'b')
    else:
        belt.insert(0, 'e')

    # Remove item falling off assembly line and count it
    result = belt.pop()
    if result == 'a':
        a_count += 1
    elif result == 'b':
        b_count += 1
    elif result == 'e':
        e_count += 1
    elif result == 'p':
        p_count += 1
    if result != "e":
        output.insert(0, result)
    print("")
    print("Output:")
    print(str(output))

    # The sleep is variable for human viewing of operations
    sleep(1)
    # Clear screen
    system('cls')

# Tally final results
print("")
print("")
print("Final results:")
print("Type A parts: " + str(a_count))
print("Type B parts: " + str(b_count))
print("Finished parts: " + str(p_count))
