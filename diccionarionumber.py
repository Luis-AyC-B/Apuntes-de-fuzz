def number_iterator():
    for i in range(1, 100000):
        yield i


numbers = number_iterator()
for _ in range(99999):
    print(next(numbers))