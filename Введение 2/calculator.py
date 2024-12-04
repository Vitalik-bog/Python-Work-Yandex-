n_1 = float(input())
n_2 = float(input())
operation = input()


if operation == '+':
    print(n_1+n_2)
elif operation == '-':
    print(n_1-n_2)
elif operation == '*':
    print(n_1*n_2)
elif operation == '/':
    if n_2 == 0:
        print('888888')
    else:
        print(n_1/n_2)
else:
    print('888888')