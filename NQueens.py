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
        queenLocations = self.state.queen_locations
        board = self.state.board
        queens = self.state.queens_placed

        rowList = list(queenLocations.keys())
        tempRow = choice(rowList)
        tempCol = choice(queenLocations.get(tempRow))
        board[tempRow][tempCol] == "0"
        queens -= 1
        if len(self.state.queen_locations.get(tempRow)) > 1:
            self.state.queen_locations.get(tempRow).remove(tempCol)
        else:
            del queenLocations[tempRow]
        
        
        newRow = randrange(0, self.n, 1)
        newCol = randrange(0, self.n, 1)

        while board[newRow][newRow] == "q" or (newRow == tempRow and newCol == tempCol):
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
           # TODO Done

            for row in range(self.n):
                qInRow = 0
                for col in range(self.n):
                    if self.board[row][col] == 'q':
                        qInRow += 1
                    if qInRow > 1:
                        print("too many in row")
                        return False

            for col in range(self.n):
                qInCol = 0
                for row in range(self.n):
                    if self.board[row][col] == 'q':
                        qInCol += 1
                    if qInCol > 1:
                        print("too many in column")
                        return False


            for row in range(self.n):
                qInDiagonal = 0
                # print(qInDiagonal)
                for col in range(self.n):
                    for i in range(self.n):
                        for j in range(self.n):
                            if ((i + j) == (row + col)) or ((i-j) == (row - col)):
                                if self.board[i][j] == 'q' and self.board[row][col] == 'q':
                                    qInDiagonal += 1
                    # if qInDiagonal > 1:
                    #     return False
                if qInDiagonal > 1:
                    print("too many in diagonals")
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