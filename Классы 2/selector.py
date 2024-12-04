class Selector:
    
    def __init__(self, numbers):
        self.numbers = numbers[:]
        
    def get_evens(self):
        return [number for number in self.numbers if number % 2 == 0]
    
    def get_odds(self):
        return [number for number in self.numbers if number % 2 != 0] 
    
