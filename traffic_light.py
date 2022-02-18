from enum import Enum

class TrafficLightColor (Enum):
    RED = 0x1
    GREEN = 0x2
    YELLOW = 0X3

class TrafficLight ():
    def __init__ (self, colors: TrafficLightColor):
        self.colors = colors
        self.color = self.colors.RED

    def getColor (self):
        return self.color

    def setColor (self, color):
        self.color = color

