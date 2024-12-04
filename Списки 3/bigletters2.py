comand = input()
string = ['', '', '', '', '']
for z in range(5):
    for i in range(len(comand)):
        if comand[i] == 'A':
            if z == 0:
                string[z] += ' * '
            if z == 1:
                string[z] += '* *'
            if z == 2:
                string[z] += '***'
            if z == 3:
                string[z] += '* *'
            if z == 4:
                string[z] += '* *'
        elif comand[i] == 'B':
            if z == 0:
                string[z] += '** '
            if z == 1:
                string[z] += '* *'
            if z == 2:
                string[z] += '** '
            if z == 3:
                string[z] += '* *'
            if z == 4:
                string[z] += '** '
        elif comand[i] == 'C':
            if z == 0:
                string[z] += ' * '
            if z == 1:
                string[z] += '* *'
            if z == 2:
                string[z] += '*  '
            if z == 3:
                string[z] += '* *'
            if z == 4:
                string[z] += ' * ' 
        elif comand[i] == 'D':
            if z == 0:
                string[z] += '** '
            if z == 1:
                string[z] += '* *'
            if z == 2:
                string[z] += '* *'
            if z == 3:
                string[z] += '* *'
            if z == 4:
                string[z] += '** '
        elif comand[i] == 'E':
            if z == 0:
                string[z] += '***'
            if z == 1:
                string[z] += '*  '
            if z == 2:
                string[z] += '** '
            if z == 3:
                string[z] += '*  '
            if z == 4:
                string[z] += '***' 
        elif comand[i] == 'F':
            if z == 0:
                string[z] += '***'
            if z == 1:
                string[z] += '*  '
            if z == 2:
                string[z] += '** '
            if z == 3:
                string[z] += '*  '
            if z == 4:
                string[z] += '*  ' 
        elif comand[i] == 'G':
            if z == 0:
                string[z] += ' **'
            if z == 1:
                string[z] += '*  '
            if z == 2:
                string[z] += '* *'
            if z == 3:
                string[z] += '* *'
            if z == 4:
                string[z] += ' **' 
        elif comand[i] == 'H':
            if z == 0:
                string[z] += '* *'
            if z == 1:
                string[z] += '* *'
            if z == 2:
                string[z] += '***'
            if z == 3:
                string[z] += '* *'
            if z == 4:
                string[z] += '* *'
        elif comand[i] == 'I':
            if z == 0:
                string[z] += '***'
            if z == 1:
                string[z] += ' * '
            if z == 2:
                string[z] += ' * '
            if z == 3:
                string[z] += ' * '
            if z == 4:
                string[z] += '***' 
        elif comand[i] == 'J':
            if z == 0:
                string[z] += ' **'
            if z == 1:
                string[z] += '  *'
            if z == 2:
                string[z] += '  *'
            if z == 3:
                string[z] += '* *'
            if z == 4:
                string[z] += ' * ' 
        elif comand[i] == 'K':
            if z == 0:
                string[z] += '* *'
            if z == 1:
                string[z] += '** '
            if z == 2:
                string[z] += '*  '
            if z == 3:
                string[z] += '** '
            if z == 4:
                string[z] += '* *' 
        elif comand[i] == 'L':
            if z == 0:
                string[z] += '*  '
            if z == 1:
                string[z] += '*  '
            if z == 2:
                string[z] += '*  '
            if z == 3:
                string[z] += '*  '
            if z == 4:
                string[z] += '***' 
        elif comand[i] == 'M':
            if z == 0:
                string[z] += '* *'
            if z == 1:
                string[z] += '***'
            if z == 2:
                string[z] += '***'
            if z == 3:
                string[z] += '***'
            if z == 4:
                string[z] += '* *' 
        elif comand[i] == 'N':
            if z == 0:
                string[z] += '* *'
            if z == 1:
                string[z] += '***'
            if z == 2:
                string[z] += '***'
            if z == 3:
                string[z] += '* *'
            if z == 4:
                string[z] += '* *' 
        elif comand[i] == 'O':
            if z == 0:
                string[z] += '***'
            if z == 1:
                string[z] += '* *'
            if z == 2:
                string[z] += '* *'
            if z == 3:
                string[z] += '* *'
            if z == 4:
                string[z] += '***' 
        elif comand[i] == 'P':
            if z == 0:
                string[z] += '***'
            if z == 1:
                string[z] += '* *'
            if z == 2:
                string[z] += '***'
            if z == 3:
                string[z] += '*  '
            if z == 4:
                string[z] += '*  ' 
        elif comand[i] == 'Q':
            if z == 0:
                string[z] += '***'
            if z == 1:
                string[z] += '* *'
            if z == 2:
                string[z] += '* *'
            if z == 3:
                string[z] += '***'
            if z == 4:
                string[z] += '***'
        elif comand[i] == 'R':
            if z == 0:
                string[z] += '** '
            if z == 1:
                string[z] += '* *'
            if z == 2:
                string[z] += '** '
            if z == 3:
                string[z] += '* *'
            if z == 4:
                string[z] += '* *' 
        elif comand[i] == 'S':
            if z == 0:
                string[z] += ' **'
            if z == 1:
                string[z] += '*  '
            if z == 2:
                string[z] += ' * '
            if z == 3:
                string[z] += '  *'
            if z == 4:
                string[z] += '** ' 
        elif comand[i] == 'T':
            if z == 0:
                string[z] += '***'
            if z == 1:
                string[z] += ' * '
            if z == 2:
                string[z] += ' * '
            if z == 3:
                string[z] += ' * '
            if z == 4:
                string[z] += ' * ' 
        elif comand[i] == 'U':
            if z == 0:
                string[z] += '* *'
            if z == 1:
                string[z] += '* *'
            if z == 2:
                string[z] += '* *'
            if z == 3:
                string[z] += '* *'
            if z == 4:
                string[z] += '***' 
        elif comand[i] == 'V':
            if z == 0:
                string[z] += '* *'
            if z == 1:
                string[z] += '* *'
            if z == 2:
                string[z] += '* *'
            if z == 3:
                string[z] += '* *'
            if z == 4:
                string[z] += ' * '
        elif comand[i] == 'W':
            if z == 0:
                string[z] += '* *'
            if z == 1:
                string[z] += '* *'
            if z == 2:
                string[z] += '* *'
            if z == 3:
                string[z] += '***'
            if z == 4:
                string[z] += '* *' 
        elif comand[i] == 'X':
            if z == 0:
                string[z] += '* *'
            if z == 1:
                string[z] += '* *'
            if z == 2:
                string[z] += ' * '
            if z == 3:
                string[z] += '* *'
            if z == 4:
                string[z] += '* *' 
        elif comand[i] == 'Y':
            if z == 0:
                string[z] += '* *'
            if z == 1:
                string[z] += '* *'
            if z == 2:
                string[z] += '* *'
            if z == 3:
                string[z] += ' * '
            if z == 4:
                string[z] += ' * ' 
        elif comand[i] == 'Z':
            if z == 0:
                string[z] += '***'
            if z == 1:
                string[z] += '  *'
            if z == 2:
                string[z] += ' * '
            if z == 3:
                string[z] += '*  '
            if z == 4:
                string[z] += '***' 
        string[z] += '  '
for i in string:
    print(i)