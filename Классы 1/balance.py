class Balance:
    
    def __init__(self):
        self.left = 0
        self.right = 0
    
    def add_right(self, data):
        self.right += data
        
    def add_left(self, data):
        self.left += data   
        
    def result(self):
        if self.left > self.right: return "L"
        elif self.left < self.right: return "R"
        else: return "="
        
