class NumbersRow:
    
    def __init__(self, row):
        
        self.numbers = row
        
    def main(self, action):
        
        data = {"make_negative":self.make_negative,
                "square":self.square,
                "strange_command":self.strange_command}
        data[action]()
        
    def make_negative(self):
        self.numbers = list(map(lambda x: -x if x > 0 else x, self.numbers))
        
    def square(self):
        self.numbers = list(map(lambda x: x**2, self.numbers))
    
    def strange_command(self):
        self.numbers = list(map(lambda x: x+1 if x % 5 == 0 else x, self.numbers))
    
    def __call__(self):
        return self.numbers
    
nr = NumbersRow([int(i) for i in input().split()])
[nr.main(input()) for i in range(int(input()))]
print(*nr())