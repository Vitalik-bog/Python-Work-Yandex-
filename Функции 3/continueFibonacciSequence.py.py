"""
�������� �������:

def continueFibonacciSequence(sequence, n): 
    for i in range(n): 
        nextElement = sequence[-1] + sequence[-2] 
        sequence = sequence + [nextElement]

��� ������ ������� � "sequence = sequence + [nextElement]". ��� ���������� ����� ����� ��������� ������.

"""
""" ���������:"""

def continueFibonacciSequence(sequence, n): 
    for i in range(n): 
        nextElement = sequence[-1] + sequence[-2] 
        sequence += [nextElement] #���������� ������������ ������.
        #����� �������� ���������� sequence.append(nextElement)