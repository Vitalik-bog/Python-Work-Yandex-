count = int(input())
numbers = []
for i in range(count):
    numbers += [int(input())]
Range = [int(input()), int(input())]
elements = numbers[Range[0]-1:Range[1]]
res = 0
for i in elements:
    res += i
print(res)
