class LeftParagraph:
    
    def __init__(self, width):
        self.width = width
        self.words = [""]
        
    def add_word(self, word):
        words = self.words
        if len(words[-1]) < self.width and len(words[-1]) + len(word) + 1 <= self.width+1:
            words[-1] += word+" "
        else: words.append(word+" ")
        
    def end(self):
        [print(word[:-1]) for word in self.words]
        
class RightParagraph:
    
    def __init__(self, width):
        self.width = width
        self.words = [""]
        
    def add_word(self, word):
        words = self.words
        if len(words[-1]) < self.width and len(words[-1]) + len(word) + 1 <= self.width+1:
            words[-1] += word+" "
        else: words.append(word+" ")
        
    def end(self):
        [print(word[:-1].rjust(self.width, " ")) for word in self.words]
    
