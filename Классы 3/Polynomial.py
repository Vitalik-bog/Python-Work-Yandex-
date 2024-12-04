class Polynomial:
    
    def __init__(self, array):
        
        self.array = array
        self.data = 0
        
    def __call__(self, x):
        self.data = 0
        self.callprocess(self.array, x)
        return self.data

    
    def callprocess(self, array, x):
        for element in range(len(array)):
            if type(array[element]) == list: self.callprocess(array[element], x)
            else:
                if element == 0: self.data += array[element]
                else: self.data += array[element]*x**element
                
    
    def __add__(self, obj):
        return Polynomial([self.array, obj.array])

