def makeanagliph(ﬁlename, delta):
    from PIL import Image
    
    original = Image.open(ﬁlename)
    corrected = original.copy()
    pixels_orig = original.load()
    pixels_corr = corrected.load()
    x, y = original.size 
            
    for i in range(x):  
        for j in range(y):
            r, g, b = pixels_orig[i, j]
            pixels_orig[i, j] = 0, g, b 
            pixels_corr[i, j] = r, 0, 0 
            
    for i in range(x-delta):  
        for j in range(y):
            r, g, b = pixels_orig[i+delta, j]
            R, G, B = pixels_corr[i, j]
            pixels_orig[i+delta, j] = R, g, b

    
    original.save("res.jpg")
