# -*- coding: utf-8 -*-
dictionary = {'А':'A', 'Б':'B', 'В':'V', 'Г':'G', 'Д':'D', 
              'Е':'E', 'Ё':'E', 'Ж':'ZH', 'З':'Z', 'И':'I', 
              'Й':'I', 'К':'K', 'Л':'L', 'М':'M', 'Н':'N', 
              'О':'O', 'П':'P', 'Р':'R', 'С':'S', 'Т':'T', 
              'У':'U', 'Ф':'F', 'Х':'KH', 'Ц':'TC', 'Ч':'CH', 
              'Ш':'SH', 'Щ':'SHCH', 'Ъ':'', 'Ы':'Y', 'Ь':'', 
              'Э':'E', 'Ю':'IU', 'Я':'IA'}
line = input()
out = ''
for symbol in line:
    if symbol.upper() in dictionary:
        if symbol.islower(): out += dictionary[symbol.upper()].lower()
        elif symbol.isupper(): out += dictionary[symbol.upper()].title()
    else: out+=symbol
print(out)