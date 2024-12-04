def mirror(arr): 
    # Было mirroredPart = arr.reverse(). В таком случае присваивается значение None, что недопустимо. 
    # Исправление таково:
    mirroredPart = arr[:]
    mirroredPart.reverse()
    arr += mirroredPart # Лишний мусор ни к чему. Старая конструкция - arr = arr + mirroredPart
    print(arr)
mirror([4, 2, 1])