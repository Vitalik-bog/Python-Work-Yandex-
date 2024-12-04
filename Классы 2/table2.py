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
        
    def delete_row(self, row):
        del self.table[row]
        self.rows -= 1
        
    def delete_col(self, col):
        for row in self.table:
            del row[col]
        self.cols -= 1
        
    def add_row(self, row):
        self.table.insert(row, [0 for _ in range(self.cols)])
        self.rows += 1
        
    def add_col(self, col):
        for row in self.table:
            row.insert(col, 0)
        self.cols += 1
            
