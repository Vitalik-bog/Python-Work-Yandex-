n = input()
n_num = int(n)
n_f = int(str(n_num)[0])
while n_f != 1:
    n_num = n_num * n_f
    n_f = int(str(n_num)[0])
    if n_num >= 1000000000:
        break
print(n_num)