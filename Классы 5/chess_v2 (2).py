WHITE = 1
BLACK = 2

# Удобная функция для вычисления цвета противника
def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


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
    board = Board()
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
        if command == 'exit':
            break
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
        self.field[0] = [
            Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
            King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        ]
        self.field[1] = [
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        ]
        self.field[6] = [
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        ]
        self.field[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        ] 

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

    def get_piece(self, row, col):
        if correct_coords(row, col):
            return self.field[row][col]
        else:
            return None
        
    def move_and_promote_pawn(self, row, col, row1, col1, char):
        if self.field[row][col].char() != "P": return False
        if not self.move_piece(row, col, row1, col1): return False
        objects = {
            "Q":Queen,
            "R":Rook,
            "B":Bishop,
            "N":Knight,
        }
        self.field[row1][col1] = objects[char](self.field[row1][col1].color)
        return True
    
    def castling0(self):
        def white(self):
            if self.field[0][4] == None or self.field[0][0] == None: return False
            if self.field[0][4].char() != "K" or  self.field[0][0].char() != "R": return False
            if self.field[0][4].alreadyMove or  self.field[0][0].alreadyMove: return False
            if self.field[0][1] == self.field[0][2] == self.field[0][3] == None:
                self.field[0][2] = self.field[0][4]
                self.field[0][4] = None
                self.field[0][3] = self.field[0][0]
                self.field[0][0] = None                
                return True
            return False
        def black(self):
            if self.field[7][4] == None or self.field[7][0] == None: return False
            if self.field[7][4].char() != "K" or  self.field[7][0].char() != "R": return False
            if self.field[7][4].alreadyMove or  self.field[7][0].alreadyMove: return False
            if self.field[7][1] == self.field[7][2] == self.field[7][3] == None:
                self.field[7][2] = self.field[7][4]
                self.field[7][4] = None
                self.field[7][3] = self.field[7][0]
                self.field[7][0] = None                
                return True
            return False
        if white(self): return True
        if black(self): return True
        return False
        
    
    def castling7(self):
        def white(self):
            if self.field[0][4] == None or self.field[0][7] == None: return False
            if self.field[0][4].char() != "K" or  self.field[0][7].char() != "R": return False
            if self.field[0][4].alreadyMove or  self.field[0][7].alreadyMove: return False
            if self.field[0][5] == self.field[0][6] == None:
                self.field[0][6] = self.field[0][4]
                self.field[0][4] = None
                self.field[0][5] = self.field[0][7]
                self.field[0][7] = None                
                return True
            return False
        def black(self):
            
            if self.field[7][4] == None or self.field[7][7] == None: return False
            if self.field[7][4].char() != "K" or  self.field[7][7].char() != "R": return False
            if self.field[7][4].alreadyMove or  self.field[7][7].alreadyMove: return False
            if self.field[7][5] == self.field[7][6] == None:
                self.field[7][6] = self.field[7][4]
                self.field[7][4] = None
                self.field[7][5] = self.field[7][7]
                self.field[7][7] = None                
                return True
            return False
        if white(self): return True
        if black(self): return True
        return False
    
    

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
        if self.field[row1][col1] is None:
            if not piece.can_move(self, row, col, row1, col1):
                return False
        elif self.field[row1][col1].get_color() == opponent(piece.get_color()):
            if not piece.can_attack(self, row, col, row1, col1):
                return False
        else:
            return False
        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        self.color = opponent(self.color)
        return True


class Rook:

    def __init__(self, color):
        self.color = color
        self.alreadyMove = False

    def get_color(self):
        return self.color

    def char(self):
        return 'R'

    def can_move(self, board, row, col, row1, col1):
        # Невозможно сделать ход в клетку, которая не лежит в том же ряду
        # или столбце клеток.
        if row != row1 and col != col1:
            return False

        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1, step):
            # Если на пути по горизонтали есть фигура
            if not (board.get_piece(r, col) is None):
                return False

        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1, step):
            # Если на пути по вертикали есть фигура
            if not (board.get_piece(row, c) is None):
                return False
        self.alreadyMove = True
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Pawn:

    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'P'

    def can_move(self, board, row, col, row1, col1):
        # Пешка может ходить только по вертикали
        # "взятие на проходе" не реализовано
        if col != col1:
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
        if row + direction == row1:
            return True

        # ход на 2 клетки из начального положения
        if (row == start_row
                and row + 2 * direction == row1
                and board.field[row + direction][col] is None):
            return True

        return False

    def can_attack(self, board, row, col, row1, col1):
        direction = 1 if (self.color == WHITE) else -1
        return (row + direction == row1
                and (col + 1 == col1 or col - 1 == col1))


class Knight:
    '''Класс коня. Пока что заглушка, которая может ходить в любую клетку.'''

    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'N'  # kNight, буква 'K' уже занята королём

    def can_move(self, board, row, col, row1, col1):
        valide = [(row+2, col-1), 
                  (row+2, col+1), 
                  (row-2, col-1), 
                  (row-2, col+1),
                  (row+1, col-2), 
                  (row-1, col-2), 
                  (row+1, col+2), 
                  (row-1, col+2),
                  ]
        return True if ((row1, col1) in valide and correct_coords(row1, col1)) and not (board.field[row1][col1] != None and board.field[row1][col1].color == self.color) else False
        

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class King:
    '''Класс короля. Пока что заглушка, которая может ходить в любую клетку.'''

    def __init__(self, color):
        self.color = color
        self.alreadyMove = False

    def get_color(self):
        return self.color

    def char(self):
        return 'K'

    def can_move(self, board, row, col, row1, col1):
        valide = [
            (row+1, col+1),
            (row-1, col-1),
            (row+1, col-1),
            (row-1, col+1),
            (row+1, col),
            (row-1, col),
            (row, col-1),
            (row, col+1)            
        ]
        
        if ((row1, col1) in valide and correct_coords(row1, col1)) and not (board.field[row1][col1] != None and board.field[row1][col1].color == self.color): 
            self.alreadyMove = True
            return True
        return False
        
    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Queen:
    '''Класс ферзя. Пока что заглушка, которая может ходить в любую клетку.'''

    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'Q'

    def can_move(self, board, row, col, row1, col1):
        f = board.get_piece(row1, col1)
        if correct_coords(row, col) and (f is None or f.color != self.color):
            if row == row1 and col == col1:
                return False
            if row1 != row and col1 != col:
                if abs(row1 - row) == abs(col1 - col):
                    step_row = 1 if (row1 > row) else -1
                    step_col = 1 if (col1 > col) else -1
                    for i in range(1, abs(row1 - row)):
                        r, c = row + step_row * i, col + step_col * i
                        if not (board.get_piece(r, c) is None):
                            return False
                    return True
                else:
                    return False
            elif row1 != row or col1 != col:
                if row != row1:
                    step = 1 if row1 - row > 0 else -1
                    for r in range(row + step, row1, step):
                        if not (board.get_piece(r, col) is None):
                            return False
                elif col != col1:
                    step = 1 if col1 - col > 0 else -1
                    for c in range(col + step, col1, step):
                        if not (board.get_piece(row, c) is None):
                            return False
                return True
            else:
                return False
        else:
            return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)   

class Bishop:
    '''Класс слона. Пока что заглушка, которая может ходить в любую клетку.'''

    def __init__(self, color):
        self.color = color
        

    def get_color(self):
        return self.color

    def char(self):
        return 'B'
    
    def checkWay(self, board, row, col, row1, col1):
        if row1 > row: row_way = [_ for _ in range(row+1, row1+1)]
        elif row1 < row: row_way = [_ for _ in range(row-1, row1-1, -1)]
        else: row_way = [row]
        
        if col1 > col: col_way = [_ for _ in range(col+1, col1+1)]
        elif col1 < col: col_way = [_ for _ in range(col-1, col1-1, -1)]
        else: col_way = [col]
        
        
        for _ in range(len(row_way)):
            x, y = row_way.pop(0), col_way.pop(0)
            if board.field[x][y] != None: return False
        return True
        
    def can_move(self, board, row, col, row1, col1):
        def base(row, col, row1, col1):
            return abs(row1 - row) == abs(col1-col) and correct_coords(row1, col1)
        
        return base(row, col, row1, col1) and (self.checkWay(board, row, col, row1, col1) or self.can_attack(board, row, col, row1, col1))        

    def can_attack(self, board, row, col, row1, col1):
        return True if board.field[row1][col1] != None and board.field[row1][col1].color != self.color else False

# __name__ -- специальная переменная, в которую python записывает имя
# файла (без .py), если этот файл импортирован из друго, и "__main__", если
# этот файл запущен как программа.
# Другими словами, следующие две строчки:
#   запустят функцию main, если файл запущен как программа;
#   не сделают ничего, если этот файл импортирован из другого.
# Второй случай реализуется, например, когда тестирующий скрипт импортирует
# классы из вашего скрипта. В этом случае функця main не будет работать
# и портить вывод теста.

#if __name__ == "__main__":
    #main()
    
