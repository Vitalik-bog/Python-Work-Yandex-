class Knight:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'N'

    def get_color(self):
        return self.color
    
    def check(self, row, col):
        return True if row in range(8) and col in range(8) else False

    def can_move(self, row, col):
        valide = [(self.row+2, self.col-1), 
                  (self.row+2, self.col+1), 
                  (self.row-2, self.col-1), 
                  (self.row-2, self.col+1),
                  (self.row+1, self.col-2), 
                  (self.row-1, self.col-2), 
                  (self.row+1, self.col+2), 
                  (self.row-1, self.col+2),
                  ]
        return True if (row, col) in valide and self.check(row, col) else False