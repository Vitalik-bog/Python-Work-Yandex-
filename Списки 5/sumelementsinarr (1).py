numbers = [int(i)**2 for i in input().split()]
data = [int(i) for i in input().split()]
print(sum(numbers[data[0]:data[1]+1]))