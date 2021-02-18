from BFS import BreadthFirstSearch
from DFS import DepthFirstSearch
from RiverCrossing import RiverCrossingProblem
from NQueens import NQueensProblem
from copy import deepcopy

def main():
    # TODO: define your RiverCrossingProblem
    leftStart = {
        "farmer": 1, 
        "wolf": 1, 
        "goat": 1, 
        "cabbage": 1
    }
    rightStart = {
        "farmer": 0, 
        "wolf": 0, 
        "goat": 0, 
        "cabbage": 0
    }
    leftEnd = {
        "farmer": 0, 
        "wolf": 0, 
        "goat": 0, 
        "cabbage": 0
    }
    rightEnd = {
        "farmer": 1, 
        "wolf": 1, 
        "goat": 1, 
        "cabbage": 1
    }
    crossing = RiverCrossingProblem()
    crossing.set_start_state(leftStart, rightStart)
    crossing.set_goal_state(leftEnd, rightEnd)
    # TODO: solve RiverCrossing via BFS
    # solutionA = BreadthFirstSearch(crossing)
    # print(BreadthFirstSearch.breadth_first_search(solutionA))
    # TODO: solve RiverCrossing via DFS
    # solutionB = DepthFirstSearch(crossing)
    # print(DepthFirstSearch.depth_first_search(solutionB))
    # TODO: define 4-Queens
    queens = NQueensProblem(5)
    # TODO: solve 4-Queens via DFS
    solutionC = DepthFirstSearch(queens)
    print(DepthFirstSearch.depth_first_search(solutionC))
    
    

    
    # TODO: solve 4-Queens via Simulated Annealing
    
    
if __name__ == '__main__':
    main()




# tempState = deepcopy(self.state)
#         queenLocations = deepcopy(self.state.queen_locations)
#         for i in range(self.n):
#             for j in range(self.n):
#                 if i in queenLocations and j in queenLocations.get(i):
#                     pass
#                 else:
#                     new_state = deepcopy(self.next_state(self.tempState, i, j))
#                     new_state.path = deepcopy(self.state.path)
#                     self.frontier.append(new_state)