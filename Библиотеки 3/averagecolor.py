from PIL import Image
 
im = Image.open("image.jpeg")
pixels = im.load() 
x, y = im.size 
size = x*y

R, G, B = 0, 0, 0
 
for i in range(x):  
    for j in range(y):
        r, g, b = pixels[i, j]
        R += int(r)
        G += int(g)
        B += int(b)
         
print(R//size, G//size, B//size)