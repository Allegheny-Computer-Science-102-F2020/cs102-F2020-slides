def integers(n):
    while True:
        yield n
        n += 1

for value in integers(10):
    print(value)
