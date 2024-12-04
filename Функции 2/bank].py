#-*-coding: utf8 -*-

transactions = []
sums = []
def getTransactions(t):
    global transactions
    if t != 'print_it':
        transactions.append(t.split('-')[1].split(':')[0])
        sums.append(t.split('-')[1].split(':')[1])
    else:
        out = []
        for element in transactions:
            if not element in out:
                count_el, summa = 0, 0
                for i in range(len(transactions)):
                    if transactions[i] == element:
                        count_el += 1
                        summa += int(sums[i])
                out += [count_el, element, summa]
                print(' '.join([str(count_el), str(element), str(summa)]))
