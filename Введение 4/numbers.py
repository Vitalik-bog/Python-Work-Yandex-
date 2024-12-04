num = int(input())
n_1 = 1
n_2 = 1
n = n_1 + n_2
print(n_1)
print(n_2)
while n <= num:
    print(n)
    n_1 = n_2
    n_2 = n
    n = n_1 + n_2