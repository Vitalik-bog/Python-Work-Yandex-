def fromStringToList(string, container):
    return [container.append(int(i)) for i in string.split()]