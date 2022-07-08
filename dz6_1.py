import time
import itertools

class TrafficLight:
    __color = [['ReD', [7, 31]], ['YeLLoW', [2, 33]], ['GrEEn', [5, 32]], ['YeLLoW', [2, 33]]]

    def running(self):
        for light in itertools.cycle(self.__color):
            print(f'\r\033[{light[1][1]}m\033[4m\033[1m{light[0]}\033[0m', end='')
            time.sleep(light[1][0])

traffic_l = TrafficLight()
traffic_l.running()
