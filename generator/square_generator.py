#3 and 5
class SquareGenerator:
    def __init__(self):
        pass

    def generate_squares(self, start, end):
        if end < start:
            raise Exception("the end of the range is less than the start")

        return [x**2 for x in range(start, end + 1)]

generator = SquareGenerator()
squares2 = generator.generate_squares(10, 1)
print(squares2)