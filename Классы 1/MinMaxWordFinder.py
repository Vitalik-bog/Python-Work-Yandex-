class MinMaxWordFinder:
    
    def __init__(self):
        self.words = {}
    
    def add_sentence(self, data):
        data = data.split()
        for word in data:
            self.words[len(word)] = self.words.get(len(word), []) + [word]
    
    def shortest_words(self):
        return sorted(list(sorted(list(self.words.items()), key=lambda pair: pair[0])[0])[1]) if len(self.words) != 0 else []
    
    def longest_words(self):
        return sorted(list(set(list(sorted(list(self.words.items()), key=lambda pair: pair[0])[-1])[1]))) if len(self.words) != 0 else []
    