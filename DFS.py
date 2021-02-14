from copy import deepcopy


# NOTE: python's default behavior on the assignment operator for objects and dictionaries is to make a shallow copy
# (i.e., add a pointer). This is not ideal for what we're doing here. Use deepcopy to make your life easier.

class DepthFirstSearch:
    def __init__(self, problem):
        self.visited = []
        self.problem = deepcopy(problem)

    def depth_first_search(self): # STUDENT SOLUTION

        # TODO: DFS is very similar to BFS; what are the main difference(s)?

        # TODO: return solved probem
        pass
