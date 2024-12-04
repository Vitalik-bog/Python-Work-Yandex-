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
        string[z] += '  '
for i in string:
    print(i)