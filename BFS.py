from copy import deepcopy
# NOTE: python's default behavior on the assignment operator for objects and dictionaries is to make a shallow copy
# (i.e., add a pointer). This is not ideal for what we're doing here. Use deepcopy to make your life easier.

class BreadthFirstSearch:
    def __init__(self, problem):
        self.visited = []
        self.problem = deepcopy(problem)

    def breadth_first_search(self): # STUDENT SOLUTION
        # TODO: loop condition: how do we know when to break out of the loop?

        # TODO: check whether we should expand the current state

        # TODO: if so, populate the frontier

        # TODO: if there is a next state in the frontier, set self.problem.state to it; otherwise, break

        # TODO: also do some bookkeeping: the new state should make it onto both self.visited and the problem's solution path

        # TODO: return solved problem
        pass


