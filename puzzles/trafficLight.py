import time

class trafficLight:

    def __init__(self, name):

        self.color = 'red'
        self.name = name

    def printName(self):

        return self.name

    def checkColor(self):

        return self.color

    def setColor(self, newColor):

        if newColor in ['red', 'yellow', 'green']:
            self.color = newColor

def printLights(lights):

    print('Traffic light status:')

    for i in lights:
        print(i.printName(), i.checkColor())

North = trafficLight('North')
West = trafficLight('West')
East = trafficLight('East')
South = trafficLight('South')

greenInterval = 10
yellowInterval = 3

Lights = [North, West, East, South]
index = 0

while True:

    # Assert other lights are red
    for i in Lights:
        if i != index:
            assert i.checkColor() == 'red'

    Lights[index].setColor('green')
    printLights(Lights)
    time.sleep(greenInterval)

    Lights[index].setColor('yellow')
    printLights(Lights)
    time.sleep(yellowInterval)

    Lights[index].setColor('red')

    index += 1
    if index > 3:
        index = 0
