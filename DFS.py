from copy import deepcopy

# NOTE: python's default behavior on the assignment operator for objects and dictionaries is to make a shallow copy
# (i.e., add a pointer). This is not ideal for what we're doing here. Use deepcopy to make your life easier.
# Only difference is the for loop - in DFS you start with the visited and go to the frontier
class DepthFirstSearch:
    def __init__(self, problem):
        self.visited = []
        self.problem = deepcopy(problem)

    def depth_first_search(self): # STUDENT SOLUTION
        self.problem.frontier.append(self.problem.start_state) # Add the start state (everything on left)
        while len(self.problem.frontier) > 0 and not self.problem.is_finished(): # While end state is not reached
            self.problem.state = deepcopy(self.problem.frontier.pop(len(self.problem.frontier) - 1)) # Get the current state
            if(self.problem.state.is_valid_state()): # if the state works
                self.problem.populate_frontier() # add the next state
                for i in self.visited: # loop through visited
                    for j in self.problem.frontier: # loop through frontier
                        if i == j: # if visited matches frontier
                            self.problem.frontier.remove(j) # remove from frontier
            self.visited.append(self.problem.state) # add visited to state
        return self.problem.state # return the state
        
