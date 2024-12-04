count = int(input())
bottles = []
for i in range(count):
    bottles += [int(input())]
Range = [int(input()), int(input())]
for i in bottles:
    if i in range(Range[0], Range[1]+1):
        print(i)