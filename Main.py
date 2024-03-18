#2

def generate_squares(start, end):
    return [x**2 for x in range(start, end + 1)]

start = 1
end = 10
squares = generate_squares(start, end)
print(squares)

#3
class SquareGenerator:
    def __init__(self):
        pass

    def generate_squares(self, start, end):

        return [x**2 for x in range(start, end + 1)]

generator = SquareGenerator()
squares = generator.generate_squares(1, 10)
print(squares)
