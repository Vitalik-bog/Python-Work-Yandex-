stack = []
for i in (input().split()):
    if i not in ['+', "-", "*", "/", "~", "!", "#", "@"]:
        stack += [int(i)]
    else:
        if i == '+':
            stack[-2] = stack[-1] + stack[-2]
            del stack[-1]
        if i == '-':
            stack[-2] = stack[-2] - stack[-1]
            del stack[-1]
        if i == '*':
            stack[-2] = stack[-1] * stack[-2]
            del stack[-1]
        if i == '/':
            stack[-2] = stack[-2] // stack[-1]
            del stack[-1]
        if i == '!':
            factorial = 1
            for i in range(1, stack[-1] + 1):
                factorial *= i
            stack[-1] = factorial
        if i == '~':
            stack[-1] = -stack[-1]
        if i == '#':
            stack += [stack[-1]]
        if i == '@':
            stack[-3], stack[-2], stack[-1] = stack[-2], stack[-1], stack[-3]
print(stack[0])