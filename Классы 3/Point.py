class Point:
    
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        
    def __eq__(self, obj):  
        return True if self.x == obj.x and self.y == obj.y else False
    
    def __ne__(self, obj):  
        return False if self.x == obj.x and self.y == obj.y else True
    


