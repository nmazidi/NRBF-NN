# Some useful utility functions that can be used anywhere
def drange(start, end, step):
    i = start
    while i < end:
        yield i
        i += step
