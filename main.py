from BFS import BreadthFirstSearch
from DFS import DepthFirstSearch
from RiverCrossing import RiverCrossingProblem
# from NQueens import NQueensProblem
from copy import deepcopy

def main():
    # TODO: define your RiverCrossingProblem
    leftStart = [{
        {"farmer": 1}, 
        {"wolf": 1}, 
        {"goat": 1}, 
        {"cabbage": 1}
    }]
    rightStart = [{
        {"farmer": 0}, 
        {"wolf": 0}, 
        {"goat": 0}, 
        {"cabbage": 0}
    }]
    leftEnd = [{
        {"farmer": 0}, 
        {"wolf": 0}, 
        {"goat": 0}, 
        {"cabbage": 0}
    }]
    rightEnd = [{
        {"farmer": 1}, 
        {"wolf": 1}, 
        {"goat": 1}, 
        {"cabbage": 1}
    }]
    crossing = RiverCrossingProblem()
    crossing.set_start_state(leftStart, rightStart)
    crossing.set_goal_state(leftEnd, rightEnd)

    print(leftStart.values())
    
    
    # TODO: solve RiverCrossing via BFS
    # TODO: solve RiverCrossing via DFS

    # TODO: define 4-Queens
    # TODO: solve 4-Queens via DFS
    # TODO: solve 4-Queens via Simulated Annealing
    pass
    
if __name__ == '__main__':
    main()




