stack = []
for i in (input().split()):
    if i not in ['+', "-", "*", "/"]:
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
            stack[-2] = stack[-2] / stack[-1]
            del stack[-1]
print(stack[0])