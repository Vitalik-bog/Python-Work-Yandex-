class ReversedList:
    
    def __init__(self, array):
        
        self.array = list(reversed(array))
        
    def __len__(self):
        return len(self.array)
    
    def __getitem__(self, key):
        return self.array[key]
    
