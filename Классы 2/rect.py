class Rectangle:
    
    def __init__(self, x, y, width, height):
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.coords = set((i, j) for j in range(y, y+height+1) for i in range(x, x+width+1))
            
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_w(self):
        return self.width
    
    def get_h(self):
        return self.height  
    
    def intersection(self, rect_obj):
        coords = set(self.coords).intersection(set(rect_obj.coords))
        if not coords: return None
        x = min(coords, key=lambda pair: pair[0])[0]
        y = min(coords, key=lambda pair: pair[1])[1]
        a = max(coords, key=lambda pair: pair[0])[0]
        b = max(coords, key=lambda pair: pair[1])[1]
        width, height = a-x, b-y
        if width == 0 or height == 0: return None
        return Rectangle(x, y, width, height)
    
	

