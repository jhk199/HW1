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
        if state.board[row][col]!='q':
            new_state = deepcopy(state)
            new_state.place_queen(row, col)
            return new_state
        else:
            raise ValueError

    def populate_frontier(self):  # STUDENT SOLUTION
        # TODO
        pass

    def move(self):  # STUDENT SOLUTION
        # TODO
        pass

    def energy(self):  # STUDENT SOLUTION
        # TODO
        pass

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
           # TODO
            pass

        def place_queen(self, row, col):
            self.board[row][col] = 'q'
            self.queens_placed += 1
            if row in self.queen_locations:
                self.queen_locations[row].append(col)
            else:
                self.queen_locations[row] = [col]
            return True


