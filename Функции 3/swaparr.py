def swap(first, second):
    data = first[:]
    first.clear()
    first += second
    second.clear()
    second += data

