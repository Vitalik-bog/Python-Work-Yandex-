numbers_1, numbers_2 = set([int(i) for i in input().split()]), set([int(i) for i in input().split()])
isset = numbers_1.intersection(numbers_2)
if isset: [print(i) for i in sorted(list(isset))]
else: print('EMPTY')