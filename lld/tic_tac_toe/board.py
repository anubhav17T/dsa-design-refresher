class Board:
    def __init__(self,size):
        self.size = size
        self.grid = [[" " for _ in range(self.size)]for _ in range(self.size)]

    def display(self):
        for i in self.grid:
            print("|".join(i))

    def make_move(self,row,column,symbol):
        if 0 <= row < self.size and 0 <= column < self.size:
            if self.grid[row][column] == " ":
                self.grid[row][column] = symbol
                return True
        return False

    def check_winner(self, symbol):
        # Check each row
        for row in self.grid:
            if all(cell == symbol for cell in row):
                return True

        # Check each column
        for col in range(self.size):
            if all(self.grid[row][col] == symbol for row in range(self.size)):
                return True

        # Check main diagonal (top-left to bottom-right)
        if all(self.grid[i][i] == symbol for i in range(self.size)):
            return True

        # Check anti-diagonal (top-right to bottom-left)
        if all(self.grid[i][self.size - 1 - i] == symbol for i in range(self.size)):
            return True

        return False

    def is_draw(self):
        return all(cell != ' ' for row in self.grid for cell in row)
    


