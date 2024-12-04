class BoundingRectangle:
    
    def __init__(self):
        self.points_x = []
        self.points_y = []
    
    def add_point(self, x, y):
        self.points_x += [x]
        self.points_y += [y]
        
    def left_x(self):
        return min(self.points_x)
    
    def right_x(self):
        return max(self.points_x)
    
    def bottom_y(self):
        return min(self.points_y)
    
    def top_y(self):
        return max(self.points_y)
    
    def width(self):
        return self.right_x() - self.left_x()
    
    def height(self):
        return self.top_y() - self.bottom_y()
    
