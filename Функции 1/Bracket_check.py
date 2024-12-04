def Bracket_check(data):
    quote_1 = 0
    quote_2 = 0
    valid = True
    for i in range(len(data)):
        if quote_1 < quote_2:
            valid = False           
        if data[i] == '(':
            quote_1 += 1      
        elif data[i] == ')':
            quote_2 += 1
    if quote_1 > quote_2 or quote_1 < quote_2:
        valid = False
    if valid:
        print('YES')
    else:
        print('NO')