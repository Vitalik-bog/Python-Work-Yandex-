class OddEvenSeparator:
    
    def __init__(self):
        self.numbers = []
        
    def add_number(self, number):
        self.numbers += [number]
        
    def even(self):
        return [number for number in self.numbers if number % 2 == 0]
    
    def odd(self):
        return [number for number in self.numbers if number % 2 != 0] 
    
