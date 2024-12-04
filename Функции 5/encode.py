# -*- coding: utf-8 -*-
def encryptCaesar(msg, shift=3):
    dictionary, abc, result = {}, list('абвгдежзийклмнопрстуфхцчшщъыьэюя'), ''
    for letter in abc:
        value = abc.index(letter)+shift
        if value >= len(abc): value = value % len(abc)
        dictionary.setdefault(letter, abc[value])    
    for letter in msg:
        if dictionary.get(letter.lower()) == None and dictionary.get(letter.upper()) == None: 
            result+= letter
            continue
        if letter.islower():
            result += dictionary.get(letter)
        else:
            result += dictionary.get(letter.lower()).upper()
    return result
    
def decryptCaesar(msg, shift=3):
    dictionary, abc, result = {}, list('абвгдежзийклмнопрстуфхцчшщъыьэюя'), ''
    for letter in abc:
        value = abc.index(letter)-shift
        if value >= len(abc): value = value % len(abc)
        dictionary.setdefault(letter, abc[value])
    for letter in msg:
        if dictionary.get(letter.lower()) == None and dictionary.get(letter.upper()) == None: 
            result+= letter
            continue
        if letter.islower():
            result += dictionary.get(letter)
        else:
            result += dictionary.get(letter.lower()).upper()
    return result 

    

