def squaresgenerator(limit):
    limit = limit + 1
    current = 0
    while current < limit:
        yield current ** 2
        current += 1

# Example usage:
squaresgen = squaresgenerator(5)
for square in squaresgen:
    print(square)
