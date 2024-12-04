operation = False
while operation != 'x':
    n_1 = int(input())
    operation = input()
    if operation == '+':
        n_2 = int(input())
        print(n_1+n_2)
    elif operation == '-':
        n_2 = int(input())
        print(n_1-n_2)
    elif operation == '*':
        n_2 = int(input())
        print(n_1*n_2)
    elif operation == '/':
        n_2 = int(input())
        if n_2 != 0:
            print(n_1//n_2)
    elif operation == '%':
        n_2 = int(input())
        if n_2 != 0:
            print(n_1%n_2)
    elif operation == '!':
        if n_1 >= 0:
            f = 1
            for i in range(1, n_1+1):
                f *= i
            print(f)
    elif operation == 'x':
        print(n_1)