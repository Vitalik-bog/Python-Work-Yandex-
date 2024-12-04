alldishes = set([input() for _ in range(int(input()))])
cooked = [set([input() for i in range(int(input()))]) for j in range(int(input()))]
cooked = cooked[0].union(*cooked[1:])
[print(dish) for dish in sorted(list(alldishes.difference(cooked)))]