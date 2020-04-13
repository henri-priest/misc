import sys
import re

def addMinutes(time, offset):

    # 720 minutes per 12 hours
    min_per_12hrs = 720

    # Enforce the time stamp pattern on the time argument
    if not re.match(r"^([1-9]|1[0,1,2]):([0-5][0-9]) [A,P]M$", time):
        print("Enter time in format [H]H:MM {AM|PM}")
        exit(1)

    # Enforce that offset is an integer
    offset = int(offset)

    print("Time: " + time + " , Type: " + str(type(time)))
    print("Offset: " + str(offset) + " , Type: " + str(type(offset)))

    hours = time.split(' ')[0].split(":")[0]
    minutes = time.split(' ')[0].split(":")[1]
    total_min = int(hours) * 60 + int(minutes)
    new_min = total_min + offset

    ampm = time.split(" ")[1]

    if abs(offset) >= min_per_12hrs:
         am_pm_flips = int( abs(offset) / min_per_12hrs )
    else:
        if new_min < 0 or new_min >= min_per_12hrs:
            am_pm_flips = 1
        else:
            am_pm_flips = 0

    if am_pm_flips % 2 != 0:
        if ampm == "AM":
            ampm = "PM"
        else:
            ampm == "PM"

    new_time = new_min % min_per_12hrs
    new_hour = int( new_time / 60)
    if new_hour == 0:
        new_hour = 12
    new_min = new_time % 60

    print("AM/PM flips: " + str(am_pm_flips))

    final_time = str(new_hour) + ":" + str(new_min).zfill(2) + " " + ampm
    return final_time

def runTests():
    assert addMinutes("9:13 AM", 200) == "12:33 PM"
    assert addMinutes("12:00 AM", 720) == "12:00 PM"
    assert addMinutes("12:00 PM", 720) == "12:00 AM"

if __name__ == "__main__":

    if  sys.argv[1] == "tests":
        runTests()
        exit(0)

    n = len(sys.argv)

    if n != 3:
        print("Requires 2 arguments")
        exit(1)

    time = sys.argv[1]
    offset = sys.argv[2]

    calculated_time = addMinutes(time, offset)
    print("New time: " + calculated_time)
