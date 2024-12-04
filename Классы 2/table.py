class Table:
    
    def __init__(self, rows, cols):
        
        self.table = [[0 for _ in range(cols)] for i in range(rows)]
        self.rows = rows
        self.cols = cols
        
    def n_rows(self):
        return self.rows
    
    def n_cols(self):
        return self.cols
    
    def get_value(self, row, col):
        return self.table[row][col] if row in range(self.rows) and col in range(self.cols) else None
    
    def set_value(self, row, col, value):
        self.table[row][col] = value    
        