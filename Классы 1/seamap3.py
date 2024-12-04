class SeaMap:
    
    def __init__(self):
        self.points = [['.' for _ in range(10)] for row in range(10)]
        self.hitted = []
        
    def shoot(self, row, col, result):
        if result == 'miss': self.points[row][col] = "*"
        elif result == 'hit': self.hit(row, col)
        elif result == 'sink': self.sink(row, col)
            
        
    def sink(self, row, col):
        self.hitted += [(row, col)]
        for x,y in self.hitted:
            if self.__check(x+1, y): self.points[x+1][y] = "*"
            if self.__check(x-1, y): self.points[x-1][y] = "*"
            if self.__check(x, y+1): self.points[x][y+1] = "*"
            if self.__check(x, y-1): self.points[x][y-1] = "*"            
            if self.__check(x+1, y+1): self.points[x+1][y+1] = "*"
            if self.__check(x-1, y-1): self.points[x-1][y-1] = "*"
            if self.__check(x+1, y-1): self.points[x+1][y-1] = "*"
            if self.__check(x-1, y+1): self.points[x-1][y+1] = "*"
        for x,y in self.hitted: self.points[x][y] = "x"
        self.hitted = []
        
    def hit(self, row, col):
        self.points[row][col] = "x"
        self.hitted.append((row, col))
        
    def cell(self, row, col):
        return self.points[row][col]
    
    def __check(self, x, y):
        if x in range(10) and y in range(10) and self.points[x][y] == '.': return True
        return False
        

