# -*- coding: utf-8 -*-

"""

Основа программы заключается на трёх функциях horizontal(), vertical(), transpose() для горизонтального, вертикального и диагонального отображения соответственно.
Еще одна функция - printed() длшя удобного вывода.
main() - главная подпрограмма.

"""

def main(size=4):
    original = [list(input().replace(' ', '')) for i in range(size)]
    print('\nОригинальный список:')
    printed(original)
    print('\nГоризонтальное отражение')
    printed(horizontal(original))
    print('\nВертикальное отражение')
    printed(vertical(original))
    print('\nТранспонирование')
    printed(transpose(original))
    print('\nОтражение вдоль горизонтали и вертикали одновременно')
    printed(horizontal(vertical(original)))
    print('\nТранспонирование, затем вертикальное отражение')
    printed(vertical(transpose(original))) # Всё, что происходит внутри скобок, делается в первую очередь.
    print('\nТранспонирование, затем горизонтальное отражение')
    printed(horizontal(transpose(original)))
    print('\nДва отражения, затем транспонирование')
    printed(transpose(vertical(horizontal(original))))
    print('\nОригинальный список:')
    printed(original)
    
def horizontal(array):
    """   Пришлось долго думать, что не так с моей функцией, и почему она изменяла оригинальный объект. Наконец вспомнил, что resultarr[:] развязывает элементы только первой вложенности. Пришлось сделать циклом - resultarr = [i[:] for i in array] .     """
    resultarr = [i[:] for i in array] 
    for row in resultarr: row.reverse()
    return resultarr

def vertical(array):
    resultarr = array[:]
    resultarr.reverse()
    return resultarr

def printed(array):
    for row in array: print(*row)
    
def transpose(array):
    arr, temp_array = [], []
    for i in range(len(array[0])):
        for element in array: temp_array.append(element[i])
        arr += [temp_array]
        temp_array = []
    return arr
main()