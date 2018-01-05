# Some useful utility functions that can be used anywhere
def drange(start, end, step):
    i = start
    while i < end:
        yield i
        i += step

def max_nested_list(list, idx):
    max = list[0][idx]
    for item in list:
        if item[idx] > max:
            max = item[idx]
    return max
