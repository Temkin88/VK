def sync_generator():
    i = 0
    while True:
        i = i + 1
        if i == 2**32:
            i = 1
        yield i


sg = sync_generator()
