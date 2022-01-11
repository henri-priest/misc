#!/bin/bash

out=$(ioreg -r -d 1 -k BatteryPercent | egrep '("BatteryPercent"|"Product") ')

name1=$(echo $out | cut -d = -f 2 | cut -d \" -f 2)
echo $name1 | grep -i mouse > /dev/null
if [[ $? -eq 0 ]]
then
    name1=Mouse
else
    name1=Keyboard
fi
percent1=$(echo $out | cut -d = -f 3)
percent1=$(echo $percent1 | cut -d ' ' -f 1)

name2=$(echo $out | cut -d = -f 4 | cut -d \" -f 2)
echo $name2 | grep -i mouse > /dev/null
if [[ $? -eq 0 ]]
then
    name2=Mouse
else
    name2=Keyboard
fi
percent2=$(echo $out | cut -d = -f 5)
percent2=$(echo $percent2 | cut -d ' ' -f 1)

echo $name1: $percent1
echo $name2: $percent2
