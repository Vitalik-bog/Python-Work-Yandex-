class Date:
    
    def __init__(self, month, day):
        
        self.month = month
        self.day = day
        self.data = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
    def __sub__(self, obj):
        
        return sum(self.data[:self.month-1])+self.day-(sum(obj.data[:obj.month-1])+obj.day)
    
