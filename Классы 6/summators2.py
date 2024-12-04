class Summator:
    
    def transform(self,n):
        
        return n
    
    def sum(self, n):
        return sum(list(map(self.transform, list(range(n+1)))))

class PowerSummator(Summator):
    
    def __init__(self, b):
        
        self.b = b

    
class SquareSummator(PowerSummator):
    
    def __init__(self):
        pass
    
    def transform(self,n):
        
        return n**2
    
    
class CubeSummator(PowerSummator):
    
    def __init__(self):
        pass    
    
    def transform(self,n):
        
        return n**3
