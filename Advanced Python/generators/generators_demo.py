def my_generator(n):
    value = 0
    while value < n:
        yield value
        value += 1

# large file processing
def read_large_file(path):
    with open(path) as f:
        for line in f:
            yield line

# Generators can be also created using generator expressions
data = (x*x for x in range(1, 11))
for d in data:
    print(d)


if __name__ == '__main__':
    gen = my_generator(10)
    for val in gen:
        print(val)
    print(next(gen))


