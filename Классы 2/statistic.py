class MinStat:
    
    def __init__(self):
        self.numbers = []
        
    def add_number(self, number):
        self.numbers.append(number)
        
    def result(self):
        return min(self.numbers) if len(self.numbers) > 0 else None
    
class MaxStat:
    
    def __init__(self):
        self.numbers = []
        
    def add_number(self, number):
        self.numbers.append(number)
        
    def result(self):
        return max(self.numbers) if len(self.numbers) > 0 else None

class AverageStat:
    
    def __init__(self):
        self.numbers = []
        
    def add_number(self, number):
        self.numbers.append(number)
        
    def result(self):
        return sum(self.numbers)/len(self.numbers) if len(self.numbers) > 0 else None
    

