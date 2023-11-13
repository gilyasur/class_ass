def myzip(it1, it2):
    iter1 = iter(it1)
    iter2 = iter(it2)
    while True:
        try:
            element1 = next(iter1)
            element2 = next(iter2)
            yield (element1, element2)
        except StopIteration:
            break



