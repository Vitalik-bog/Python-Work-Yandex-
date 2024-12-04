"""
Крайне любопытный фильтр. На выходе получается смесь ярких цветов. Решил поэкперементировать со случайными цветами.
Соседние пиксели не использовал, поэтому рекомендую тестировать содержимое функции напрямую, а не через её вызов.
"""

def image_ﬁlter(pixels, i, j):
    from random import randint
    from PIL import Image
   # im = Image.open("image.jpg")
    #pixels = im.load() 
    #x, y = im.size     
    #for i in range(x): 
      #  for j in range(y):
    r, g, b = pixels[i, j]
    pixels[i, j] = tuple(sorted([g+i, b+randint(1, 15), r+j], key=lambda x: str(x)))
    #im.save("res.jpg")
