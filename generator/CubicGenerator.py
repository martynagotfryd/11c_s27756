# 8
from generator.SquareGenerator import SquareGenerator
class CubicGenerator(SquareGenerator):
    def __init__(self):
        super().__init__()

    def generate_cubes(self, start, end):
        if end < start:
            raise Exception("the end of the range is less than the start")

        return [x**3 for x in range(start, end+1)]

    def generate_squares(self, start, end):
        if end < start:
            raise Exception("the end of the range is greater than the start")

        return [x**2 for x in range(start, end + 1)]

generator = CubicGenerator()
cubics = generator.generate_cubes(1, 10)
print(cubics)

generator = SquareGenerator()
squares2 = generator.generate_squares(1, 10)
print(squares2)