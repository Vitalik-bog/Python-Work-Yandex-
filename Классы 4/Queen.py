class Queen:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'Q'

    def get_color(self):
        return self.color
    
    def check(self, row, col):
        return True if row in range(8) and col in range(8) else False

    def can_move(self, row, col):
        return True if (abs(row - self.row) == abs(col-self.col) or self.col == col or self.row == row) and self.check(row, col) else False    