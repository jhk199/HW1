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
        
        return self.state.is_valid_state() and self.state.queens_placed == self.n

    def next_state(self, state, row, col):
        if state.board[row][col] != 'q':
            new_state = deepcopy(state)
            new_state.place_queen(row, col)
            return new_state
        else:
            raise ValueError

    def populate_frontier(self):  # STUDENT SOLUTION
        # TODO Done
        tempState = deepcopy(self.state)
        queenLocations = deepcopy(tempState.queen_locations)
        if tempState.queens_placed < self.n:
            for row in range(self.n):
                for col in range(self.n):
                    #checks if a queen is already in place at location
                    if row in queenLocations and col in queenLocations.get(row):
                        pass
                    #if no queen is in place, the possible location for the queen is recorded in the frontier
                    else:
                        newState = self.next_state(tempState, row, col)
                        newState.path = deepcopy(self.state.path)
                        newState.path.append(newState)
                        self.frontier.append(newState)



    def move(self):  # STUDENT SOLUTION
        previousRows = list(self.state.queen_locations.keys())
        # print(len(previousRows))
 
        tempRow = choice(previousRows)
        tempCol = choice(self.state.queen_locations.get(tempRow))
 
        self.state.board[tempRow][tempCol] = '0'
        self.state.queens_placed -= 1
        if len(self.state.queen_locations.get(tempRow)) > 1:
            self.state.queen_locations.get(tempRow).remove(tempCol)
        else:
            del self.state.queen_locations[tempRow]
        
        
        newRow = randrange(0, self.n, 1)
        newCol = randrange(0,self.n, 1)
 
        while self.state.board[newRow][newCol] == 'q' or (newRow == tempRow and newCol == tempCol):
            newRow = randrange(0, self.n, 1)
            newCol = randrange(0, self.n, 1)
 
        self.state.place_queen(newRow, newCol)


    def energy(self):  # STUDENT SOLUTION
        # TODO
        temperature = 0
        usedRows = []
        usedCols = []
        usedDiagonals = {}
        usedSums = []
        usedDiffs = []
        for row in range(self.n):
            for col in range(self.n):
                if self.state.board[row][col] == 'q':
                    if row in usedRows:
                        temperature += 2
                    else:
                        usedRows.append(row)
                    if col in usedCols:
                        temperature += 6
                    else:
                        usedCols.append(col)          
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
            # Brute Forcing Row Check
            for row in range(self.n):
                qRow = 0
                for col in range(self.n):
                    if self.board[row][col] == 'q':
                        qRow += 1
                    if qRow > 1:
                        return False
            # Brute Forcing Row Check     
            for col in range(self.n):
                qCol = 0
                for row in range(self.n):
                    if self.board[row][col] == 'q':
                        qCol += 1
                    if qCol > 1:
                        return False
            # Brute Forcing Diagonal Check
            for row in range(self.n):
                qDiagonal = 0
                for col in range(self.n):
                    for i in range(self.n):
                        for j in range(self.n):
                            if ((i + j) == (row + col)) or ((i-j) == (row - col)):
                                if self.board[i][j] == 'q' and self.board[row][col] == 'q':
                                    qDiagonal += 1
                if qDiagonal > 1:
                    return False
            return True

        def place_queen(self, row, col):
            self.board[row][col] = 'q'
            self.queens_placed += 1
            if row in self.queen_locations:
                self.queen_locations[row].append(col)
            else:
                self.queen_locations[row] = [col]
            return True