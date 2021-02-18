from copy import deepcopy
from random import randrange, shuffle, choice
from simanneal import Annealer


# NOTE: python's default behavior on the assignment operator for objects and dictionaries is to make a shallow copy
# (i.e., add a pointer). This is not ideal for what we're doing here. Use deepcopy to make your life easier.


class NQueensProblem(Annealer):

    def __init__(self, n):
        self.start_state = self.NQueensState(n)
        self.state = deepcopy(self.start_state)
        self.n = n
        self.frontier = []

    def is_finished(self):
        self.move()
        return self.state.is_valid_state() and self.state.queens_placed == self.n

    def next_state(self, state, row, col):
        if state.board[row][col]!='q':
            new_state = deepcopy(state)
            new_state.place_queen(row, col)
            return new_state
        else:
            raise ValueError

    def populate_frontier(self):  # STUDENT SOLUTION
        tempState = deepcopy(self.state)
        queenLocations = deepcopy(self.state.queen_locations)
        for i in range(self.n):
            for j in range(self.n):
                if i in queenLocations and j in queenLocations.get(i):
                    pass
                else:
                    new_state = deepcopy(self.next_state(tempState, i, j))
                    new_state.path = deepcopy(self.state.path)
                    self.frontier.append(new_state)
                    

    def move(self):  # STUDENT SOLUTION
        queenLocations = self.state.queen_locations
        board = self.state.board
        queens = self.state.queens_placed

        rowList = list(queenLocations.keys())
        tempRow = choice(rowList)
        tempCol = choice(queenLocations.get(tempRow))
        board[tempRow][tempCol] == "0"
        queens -= 1
        del queenLocations[tempRow]
        
        newRow = randrange(0, self.n, 1)
        newCol = randrange(0, self.n, 1)

        while board[newRow][newRow] == "q" or (newRow == tempRow and newCol == tempCol):
            newRow = randrange(0, self.n, 1)
            newCol = randrange(0, self.n, 1)
        
        self.state.place_queen(newRow, newCol)
        

    def energy(self):  # STUDENT SOLUTION
        temperature = 0
        queens = deepcopy(self.state.queen_locations)
        for i in range(self.state.queens_placed):
            for j in range(self.state.queens_placed):
                if queens.get(i) == queens.get(j) or (i - j) == (queens.get(i) - queens.get(j)):
                    temperature += 1
        return temperature

    class NQueensState():
        def __init__(self, n):
            self.n = n
            self.board = [['0' for i in range(n)] for j in range(n)]
            self.queens_placed = 0
            self.queen_locations = {}
            self.path = []

        def __repr__(self):
            new = '\n'
            return f'{new.join(str(x) for x in self.board)}'

        def is_valid_state(self):  # STUDENT SOLUTION
            colCount = []
            rowCount = []
            diagCount = []
            revDiagCount = []
            for row in range(self.n):
                for col in range(self.n):
                    if self.board[row][col] == 'q':
                        if(rowCount.count(row) > 0):
                            return False
                        rowCount.append(row)
                        if(colCount.count(col) > 0):
                            return False
                        colCount.append(col)
                        if (diagCount.count(row - col) > 0):
                            return False
                        diagCount.append(row - col)
                        if (revDiagCount.count(row + col) > 0):
                            return False
                        revDiagCount.append(row + col)            
            return True


        def place_queen(self, row, col):
            self.board[row][col] = 'q'
            self.queens_placed += 1
            if row in self.queen_locations:
                self.queen_locations[row].append(col)
            else:
                self.queen_locations[row] = [col]
            return True


