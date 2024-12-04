number = float(input())
if abs(number) < 0.000001 or number == 0:
    print(1000000)
else:
    print(1/number)