WHITE = 1
BLACK = 2
board_main = None
# Удобная функция для вычисления цвета противника
def opponent(color):
    return BLACK if color == WHITE else WHITE

def print_board(board): # Распечатать доску в текстовом виде (см. скриншот)
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row, end='  ')
        for col in range(8):
            print('|', board.cell(row, col), end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        print(col, end='    ')
    print()

def main():
    # Создаём шахматную доску
    global board_main
    board = Board()
    board_main = board
    # Цикл ввода команд игроков
    while True:
        # Выводим положение фигур на доске
        print_board(board)
        # Подсказка по командам
        print('Команды:')
        print('    exit                               -- выход')
        print('    move <row> <col> <row1> <row1>     -- ход из клетки (row, col)')
        print('                                          в клетку (row1, col1)')
        # Выводим приглашение игроку нужного цвета
        if board.current_player_color() == WHITE:
            print('Ход белых:')
        else:
            print('Ход чёрных:')
        command = input()
        if command == 'exit': break
        move_type, row, col, row1, col1 = command.split()
        row, col, row1, col1 = int(row), int(col), int(row1), int(col1)
        if board.move_piece(row, col, row1, col1):
            print('Ход успешен')
        else:
            print('Координаты некорректы! Попробуйте другой ход!')

def correct_coords(row, col):
    '''Функция проверяет, что координаты (row, col) лежат
    внутри доски'''
    return 0 <= row < 8 and 0 <= col < 8

class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        for col in range(8):
            self.field[1][col] = Pawn(1, col, WHITE)
        for col in range(8):
            self.field[6][col] = Pawn(6, col, BLACK)
        self.field[0][2] = Bishop(0, 2, WHITE)  
        self.field[0][5] = Bishop(0, 5, WHITE)  
        self.field[7][2] = Bishop(7, 2, BLACK)  
        self.field[7][5] = Bishop(7, 5, BLACK)  
        
        self.field[0][1] = Knight(0, 1, WHITE)  
        self.field[0][6] = Knight(0, 6, WHITE)  
        self.field[7][1] = Knight(7, 1, BLACK)  
        self.field[7][6] = Knight(7, 6, BLACK)  
        
        self.field[0][0] = Rook(0, 0, WHITE)  
        self.field[0][7] = Rook(0, 7, WHITE)  
        self.field[7][0] = Rook(7, 0, BLACK)  
        self.field[7][7] = Rook(7, 7, BLACK)  
        
        self.field[0][3] = Queen(0, 3, WHITE)  
        self.field[7][3] = Queen(7, 3, BLACK)  
        

    
    def is_under_attack(self, r, c, color):
        for row in range(8):
            for col in range(8):
                if self.field[row][col] != None:
                    if self.field[row][col].get_color() == color:
                            if self.field[row][col].can_move(r, c): return True

        return False
                
                
    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        '''Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела.'''
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def move_piece(self, row, col, row1, col1):
        '''Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернёт True.
        Если нет --- вернёт False'''

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not piece.can_move(row1, col1):
            return False
        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True

class Pawn:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'P'

    def get_color(self):
        return self.color
    
    def checkWay(self, row, col):
        if self.color == 1:
            for row_way in range(self.row+1, row+1):
                if board_main.field[row_way][col] != None: return False
            return True
        elif self.color == 2:
            for row_way in range(self.row-1, row-1, -1):
                if board_main.field[row_way][col] != None: return False
            return True
        
    
    def kill(self, row, col):
        if board_main.field[row][col] != None and board_main.field[row][col].color != self.color:
            if self.color == 1: valide = [(self.row+1, self.col-1), (self.row+1, self.col+1)]
            else: valide = [(self.row-1, self.col+1), (self.row-1, self.col-1)]
            return True if (row, col) in valide and correct_coords(row, col) else False
        return False

    def can_move(self, row, col):
        # Пешка может ходить только по вертикали
        # "взятие на проходе" не реализовано
        if (self.col != col or not self.checkWay(row, col)) and not self.kill(row, col):
            return False

        # Пешка может сделать из начального положения ход на 2 клетки
        # вперёд, поэтому поместим индекс начального ряда в start_row.
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        # ход на 1 клетку
        if self.row + direction == row:
            return True

        # ход на 2 клетки из начального положения
        if self.row == start_row and self.row + 2 * direction == row:
            return True

        return False

class Rook:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'R'

    def get_color(self):
        return self.color
    
    def kill(self, row, col):
        return board_main.field[row][col] != None and board_main.field[row][col].color != self.color  
    
    def checkWay(self, row, col):
        if self.row == row:
            if col > self.col:
                for col_way in range(self.col+1, col+1):
                    if board_main.field[row][col_way] != None: return False
                return True
            if col < self.col:
                for col_way in range(self.col-1, col-1, -1):
                    if board_main.field[row][col_way] != None: return False
                return True
        if self.col == col:
            if row > self.row:
                for row_way in range(self.row+1, row+1):
                    if board_main.field[row_way][col] != None: return False
                return True
            if row < self.row:
                for row_way in range(self.row-1, row-1, -1):
                    if board_main.field[row_way][col] != None: return False
                return True
            
                
        
        
    def can_move(self, row, col):
       
        def base(self, row, col):
            return (self.row == row or self.col == col)
        
        return base(self, row, col) and (self.checkWay(row, col) or self.kill(row, col))

        
    
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
        return True if ((row, col) in valide and correct_coords(row, col)) and not (board_main.field[row][col] != None and board_main.field[row][col].color == self.color) else False
    
class Bishop:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'B'

    def get_color(self):
        return self.color
    
    def checkWay(self, row, col):
        if row > self.row: row_way = [_ for _ in range(self.row+1, row+1)]
        elif row < self.row: row_way = [_ for _ in range(self.row-1, row-1, -1)]
        
        if col > self.col: col_way = [_ for _ in range(self.col+1, col+1)]
        elif col < self.col: col_way = [_ for _ in range(self.col-1, col-1, -1)]
        
        
        for _ in range(len(row_way)):
            if board_main.field[row_way.pop(0)][col_way.pop(0)] != None: return False
        return True
        
        
    def kill(self, row, col):
        return True if board_main.field[row][col] != None and board_main.field[row][col].color != self.color else False
                
    
    def check(self, row, col):
        return True if row in range(8) and col in range(8) else False

    def can_move(self, row, col):
        
        def base(self, row, col):
            return abs(row - self.row) == abs(col-self.col) and self.check(row, col)
        
        return base(self, row, col) and (self.checkWay(row, col) or self.kill(row, col))
    
    
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
    
    
    def checkWay(self, row, col):
        if abs(row - self.row) == abs(col-self.col):
            if row > self.row: row_way = [_ for _ in range(self.row+1, row+1)]
            elif row < self.row: row_way = [_ for _ in range(self.row-1, row-1, -1)]
            
            if col > self.col: col_way = [_ for _ in range(self.col+1, col+1)]
            elif col < self.col: col_way = [_ for _ in range(self.col-1, col-1, -1)]
            
            
            for _ in range(len(row_way)):
                if board_main.field[row_way.pop(0)][col_way.pop(0)] != None: return False
            return True            
        elif self.col == col or self.row == row:
            if self.row == row:
                if col > self.col:
                    for col_way in range(self.col+1, col+1):
                        if board_main.field[row][col_way] != None: return False
                    return True
                if col < self.col:
                    for col_way in range(self.col-1, col-1, -1):
                        if board_main.field[row][col_way] != None: return False
                    return True
            if self.col == col:
                if row > self.row:
                    for row_way in range(self.row+1, row+1):
                        if board_main.field[row_way][col] != None: return False
                    return True
                if row < self.row:
                    for row_way in range(self.row-1, row-1, -1):
                        if board_main.field[row_way][col] != None: return False
                    return True
        return False
    
    def kill(self, row, col):
        return True if board_main.field[row][col] != None and board_main.field[row][col].color != self.color else False    

    def can_move(self, row, col):
        
        def base(self, row, col):
            return (abs(row - self.row) == abs(col-self.col) or self.col == col or self.row == row) and self.check(row, col)
        
        return base(self, row, col) and (self.checkWay(row, col) or self.kill(row, col))
    
    

# __name__ -- специальная переменная, в которую python записывает имя
# файла (без .py), если этот файл импортирован из друго, и "__main__", если
# этот файл запущен как программа.
# Другими словами, следующие две строчки:
#   запустят функцию main, если файл запущен как программа;
#   не сделают ничего, если этот файл импортирован из другого.
# Второй случай реализуется, например, когда тестирующий скрипт импортирует
# классы из вашего скрипта. В этом случае функця main не будет работать
# и портить вывод теста.

if __name__ == "__main__": main()
