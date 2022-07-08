class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def full_road_area(self, mass=25, depth=5):  # как арг. метода
        return f'Строим дорогу: {self._length} M * {self._width} М * {mass} КГ * {depth} СМ = ' f'{(self._length * self._width * mass * depth) / 1000}'


road_1 = Road(5000, 20)
print(road_1.full_road_area())

road_2 = Road(2500, 15)
print(road_2.full_road_area())
