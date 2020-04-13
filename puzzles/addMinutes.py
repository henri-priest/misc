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

    # Break out hours/minutes and calc offset (since it loops around ever 12hrs)
    hours = time.split(' ')[0].split(":")[0]
    minutes = time.split(' ')[0].split(":")[1]
    total_min = int(hours) * 60 + int(minutes)
    new_min = total_min + offset

    # Current AM/PM value
    ampm = time.split(" ")[1]

    # Calculate how many times AM/PM rolls over
    if abs(offset) >= min_per_12hrs:
         am_pm_flips = int( abs(offset) / min_per_12hrs )
    else:
        if offset >= 0:
            if (new_min < 0 or new_min >= min_per_12hrs) and hours != "12":
                am_pm_flips = 1
            else:
                am_pm_flips = 0
        else:
            if (new_min < 0) or (hours == "12" and new_min < min_per_12hrs):
                am_pm_flips = 1
            else:
                am_pm_flips = 0

    # Only change AM/PM on odd numbered rollovers                
    if am_pm_flips % 2 != 0:
        if ampm == "AM":
            ampm = "PM"
        else:
            ampm = "AM"

    # Calculate new time Value
    new_time = new_min % min_per_12hrs
    new_hour = int( new_time / 60)
    if new_hour == 0:
        new_hour = 12
    new_min = new_time % 60

    # Stuff new time value back into original format and return
    final_time = str(new_hour) + ":" + str(new_min).zfill(2) + " " + ampm
    return final_time

def runTests():
    assert addMinutes("9:13 AM", 200) == "12:33 PM"
    assert addMinutes("9:13 AM", -1) == "9:12 AM"
    assert addMinutes("9:13 AM", 1) == "9:14 AM"
    assert addMinutes("9:13 AM", 166) == "11:59 AM"
    assert addMinutes("9:13 AM", 167) == "12:00 PM"
    assert addMinutes("9:13 AM", 168) == "12:01 PM"
    assert addMinutes("9:13 AM", -552) == "12:01 AM"
    assert addMinutes("9:13 AM", -553) == "12:00 AM"
    assert addMinutes("9:13 AM", -554) == "11:59 PM"

    assert addMinutes("12:00 AM", -720) == "12:00 PM"
    assert addMinutes("12:00 AM", 720) == "12:00 PM"
    assert addMinutes("12:00 AM", 1439) == "11:59 PM"
    assert addMinutes("12:00 AM", 1440) == "12:00 AM"
    assert addMinutes("12:00 AM", 1441) == "12:01 AM"
    assert addMinutes("12:00 AM", 2159) == "11:59 AM"
    assert addMinutes("12:00 AM", 2160) == "12:00 PM"
    assert addMinutes("12:00 AM", 2161) == "12:01 PM"
    assert addMinutes("12:00 AM", 60) == "1:00 AM"

    assert addMinutes("12:00 PM", 720) == "12:00 AM"
    assert addMinutes("12:00 PM", -720) == "12:00 AM"
    assert addMinutes("12:00 PM", -1440) == "12:00 PM"
    assert addMinutes("12:00 PM", 1439) == "11:59 AM"
    assert addMinutes("12:00 PM", 1440) == "12:00 PM"
    assert addMinutes("12:00 PM", 1441) == "12:01 PM"
    assert addMinutes("12:00 PM", 2159) == "11:59 PM"
    assert addMinutes("12:00 PM", 2160) == "12:00 AM"
    assert addMinutes("12:00 PM", 2161) == "12:01 AM"
    assert addMinutes("12:00 PM", 60) == "1:00 PM"

    assert addMinutes("11:59 AM", 0) == "11:59 AM"
    assert addMinutes("11:59 AM", 1) == "12:00 PM"
    assert addMinutes("11:59 AM", 2) == "12:01 PM"

    assert addMinutes("11:59 PM", 0) == "11:59 PM"
    assert addMinutes("11:59 PM", 1) == "12:00 AM"
    assert addMinutes("11:59 PM", 2) == "12:01 AM"

    assert addMinutes("12:01 PM", -2) == "11:59 AM"
    assert addMinutes("12:01 PM", -1) == "12:00 PM"
    assert addMinutes("12:01 PM", 0) == "12:01 PM"

    assert addMinutes("12:01 AM", -2) == "11:59 PM"
    assert addMinutes("12:01 AM", -1) == "12:00 AM"
    assert addMinutes("12:01 AM", 0) == "12:01 AM"

    print("All tests passed...")

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
