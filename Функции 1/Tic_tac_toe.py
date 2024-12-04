def Tic_tac_toe(data):
    lines = [''.join(i).replace(' ', '') for i in data]
    win = 'draw'
    for line in lines:
        if 'xxx' in line:
            win ='x'
            break
        if '000' in line:
            win = '0'
            break
    if win == 'draw':
        for j in range(3):
            if lines[0][j] == 'x' and lines[1][j] == 'x' and lines[2][j] == 'x':
                win = 'x'
            elif lines[0][j] == '0' and lines[1][j] == '0' and lines[2][j] == '0':
                win = '0'
    if win == 'draw':
        if lines[0][0] == 'x' and lines[1][1] == 'x' and lines[2][2] == 'x':
            win = 'x'
        elif lines[0][2] == 'x' and lines[1][1] == 'x' and lines[2][0] == 'x':
            win = 'x'
    if win == 'draw':
        if lines[0][0] == '0' and lines[1][1] == '0' and lines[2][2] == '0':
            win = '0'
        elif lines[0][2] == '0' and lines[1][1] == '0' and lines[2][0] == '0':
            win = '0'        
    if win != 'draw':        
        print(win, 'win')
    else:
        print(win)    