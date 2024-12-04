#-*-coding: utf8 -*-
persons = {}
def addFriends(nameOfPerson, listOfFriends):
    global persons
    if not nameOfPerson in persons:
        persons.update({nameOfPerson: listOfFriends})
    else:
        persons.update({nameOfPerson: persons.get(nameOfPerson) + listOfFriends})

def isFriends(nameOfPerson1, nameOfPerson2):
    #print(persons)
    for p in persons:
        if p == nameOfPerson1 and nameOfPerson2 in persons.get(nameOfPerson1):
            print(True)
            return
        if p == nameOfPerson2 and nameOfPerson1 in persons.get(nameOfPerson2):
            print(True)
            return
    print(False)
def printFriends(nameOfPerson):
    arr = persons.get(nameOfPerson)
    arr.sort()
    print(' '.join(arr))
