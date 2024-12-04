class BigBell:
    
    def __init__(self):
        self.word = True
        
    def sound(self):
        if self.word: print("ding")
        else: print("dong")
        self.word = not self.word
        
