import math

#2
def generate_squares(start, end):
    return [x**2 for x in range(start, end + 1)]

start = 1
end = 10
squares1 = generate_squares(start, end)
print(squares1)


#4
squereRoots = [math.sqrt(x) for x in squares1]
print(squereRoots)


