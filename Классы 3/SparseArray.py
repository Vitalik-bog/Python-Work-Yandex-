class SparseArray:
    
    def __init__(self):
        
        self.array = {}
        
    def __setitem__(self, key, value):
        
        self.array[key] = value
        
    def __getitem__(self, key):
        
        return self.array.get(key, 0)  
    
