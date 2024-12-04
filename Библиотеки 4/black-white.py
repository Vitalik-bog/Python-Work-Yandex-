from PIL import Image
import numpy as np
image = np.asarray(Image.open('image.jpg'))
x, y, colors = image.shape
obj = image
obj = obj.reshape(x*y, colors)
obj = obj.transpose()

obj = np.array([np.round(obj[0] * 0.2989 + obj[1] * 0.5870 + obj[2] * 0.1140)] * 3)

obj = obj.transpose() 
obj = obj.reshape(x, y, colors)

Image.fromarray(np.uint8(obj)).save('res.jpg')