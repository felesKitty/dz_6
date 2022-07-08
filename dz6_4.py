from random import choice

class Car:
    direction = ['right', 'left', 'forward', 'back']

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'The color of car {name} is {color}. Is it a police car? {is_police}')

    def go(self):
        print('This car went.')

    def stop(self):
        print('This car stop.')

    def turn_direction(self):
        print(f'This car turn {choice(self.direction)}.')

    def show_speed(self):
        print(f'Speed of this car is: {self.speed}.')


class TownCar(Car):
    def show_speed(self):
        if int(self.speed) > 60:
            print('You were speeding!')
        else:
            super().show_speed()

class SportCar(Car):
    '''wzhuuuh'''


class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) > 40:
            print('You were speeding!')
        else:
            super().show_speed()

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


town_c = TownCar(65, 'green', 'Bi-bi')
sport_c = SportCar(140, 'yellow', 'Wow')
work_c = WorkCar(38, 'light-blue', 'Refrigerator')
pol_c = PoliceCar(55, 'white with strips', 'Go away!')
print()

all_cars_list = [town_c, sport_c, work_c, pol_c]

for v in all_cars_list:
    v.go()
    v.show_speed()
    v.turn_direction()
    v.stop()
    print()
