def arithmeticOperation(operation):
    if operation == '+': return lambda x, y: x + y
    elif operation == '-': return lambda x, y: x - y
    elif operation == '*': return lambda x, y: x * y
    elif operation == '/': return lambda x, y: x / y
