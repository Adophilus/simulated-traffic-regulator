from traffic_light import TrafficLight
from time import sleep

class TrafficLightController ():
    def __init__ (self, no_of_lanes, timeout = 10):
        self.no_of_lanes = no_of_lanes
        self.timeout = timeout

    def run (self):
        lanes = [
                [0, 0]
        ] * self.no_of_lanes
        while (True):
            for i in range(len(lanes)):
                """
                if [ 0, 1 ] -> [ 1, 1 ]
                then
                    [ 2, 0 ] -> [ 0, 0 ]
                    [ 1, 0 ] -> [ 2, 1 ]
                fi

                if  [ 

                """
                pass
if __name__ == "__main__":
    trafficController = TrafficLightController(3)
    trafficController.run()
