peoples = int(input())
thisiq = False
dataiq = False
for i in range(1, peoples + 1):
    thisiq = int(input())
    dataiq += thisiq
    if dataiq / i > thisiq:
        print('<')
    elif dataiq / i < thisiq:
        print('>')
    elif dataiq / i == thisiq:
        print('0')