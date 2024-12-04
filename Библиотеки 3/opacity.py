from PIL import Image
 
im = Image.open(input())
im_2 = Image.open(input())
pixels_1 = im.load() 
pixels_2 = im_2.load() 
x, y = im.size 
 
for i in range(x):  
    for j in range(y):
        r, g, b = pixels_1[i, j]
        R, G, B = pixels_2[i, j]
        R = int(0.5*r + 0.5*R) 
        G = int(0.5*g + 0.5*G)
        B = int(0.5*b + 0.5*B) 
        pixels_2[i, j] = R, G, B
         
im_2.save("res.jpg")