"""

������������ �������:

numbers = [2, 5, 7, 7, 8, 4, 1, 6] 
odd = even = []
for number in numbers: 
   if number % 2 == 0: 
       even.append(number) 
   else: 
       odd.append(number)
       
������ ������� � ������� "odd = even = []". ��������� ������ ��������� ������ � �������� �����, � ��������� ���� ��������������� ������ odd � even �� ������ ��������� �� ���� ������!

"""


"""���������� �������:"""

numbers = [2, 5, 7, 7, 8, 4, 1, 6] 
odd, even = [], []; """������ ��������� ��� ������ �������."""
for number in numbers: 
    if number % 2 == 0: 
        even.append(number) ;"""��������� � ������ even, odd ��� ���� �� ��������."""
    else: 
        odd.append(number)  ;"""��������� � ������ odd, even ��� ���� �� ��������."""