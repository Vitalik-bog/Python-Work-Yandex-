"""
Неверный вариант:

def continueFibonacciSequence(sequence, n): 
    for i in range(n): 
        nextElement = sequence[-1] + sequence[-2] 
        sequence = sequence + [nextElement]

Вся ошибка кроется в "sequence = sequence + [nextElement]". Так появляется очень много ненужного мусора.

"""
""" Правильно:"""

def continueFibonacciSequence(sequence, n): 
    for i in range(n): 
        nextElement = sequence[-1] + sequence[-2] 
        sequence += [nextElement] #изменяется существующий объект.
        #Также возможна реализация sequence.append(nextElement)