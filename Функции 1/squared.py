def squared():
    string = ''
    for i in range(11, 100):
        if i**2 % 100 != 0:
            string += str(str(i**2)).ljust(5, ' ')
            if len(string.split()) % 9 == 0:
                if i in [19, 29]:
                    s = 2
                else:
                    s = 1
                print(string[:-s])
                string = ''