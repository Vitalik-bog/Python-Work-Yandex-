products = set([input() for _ in range(int(input()))])
dishes = {}
for i in range(int(input())):
    dish = input().split()
    dishes[dish[0]] = set([input() for i in range(int(dish[1]))])
for dish in dishes.items():
    if dish[1] <= products: print(dish[0])