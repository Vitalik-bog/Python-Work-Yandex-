from sys import stdin
from random import choice

peoples = [' '.join(line.split()) for line in stdin]
friends = []
for person in peoples:
    friend = choice(peoples)
    while friend == person or friend in friends: friend = choice(peoples)
    friends.append(friend)
    #peoples.pop(peoples.index(friend))
for person in range(len(friends)):
    print(peoples[person], '-', friends[person])