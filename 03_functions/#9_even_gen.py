def even_gen(limit):
    for i in range(2, limit + 1, 2):
        yield i

for num in even_gen(10):
    print(num)