class MyIterator:
    def __init__(self, limit):
        self.limit = limit+1
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        square = self.current
        self.current += 1
        return square

# Example usage:
squares_iter = MyIterator(5)
for square in squares_iter:
    print(square)
