from copy import deepcopy


# NOTE: python's default behavior on the assignment operator for objects and dictionaries is to make a shallow copy
# (i.e., add a pointer). This is not ideal for what we're doing here. Use deepcopy to make your life easier.

class RiverCrossingProblem:

    def __init__(self):
        self.start_state = None
        self.goal_state = None
        self.state = None
        self.frontier = []

    def __repr__(self):
        return f'A{" complete" if self.is_finished() else "n incomplete"} RiverCrossingPuzzle. ' \
               f'\nCurrent state is: {self.state}. \nGoal state is: {self.goal_state}\n'

    def set_start_state(self, left, right):
        self.start_state = self.RiverCrossingState(left, right)
        self.state = deepcopy(self.start_state)

    def set_goal_state(self, left, right):
        self.goal_state = self.RiverCrossingState(left, right)

    def is_finished(self):
        return self.state == self.goal_state

    def next_state(self, state, item):  # STUDENT SOLUTION
        new_state = deepcopy(state)
        if item == "farmer":
            if(state.left_bank[item] == 1):
                new_state.path.append(state)
                new_state.move_to_right(item)
                print("Item: ", item, " (farmer moves from left to right)")
                return new_state
            else: 
                new_state.path.append(state)
                new_state.move_to_left(item)
                print("Item: ", item, " (farmer moves from right to left")
                return new_state
        elif state.left_bank["farmer"] == 1 and state.left_bank[item] == 1:
            new_state.path.append(state)
            new_state.move_to_right("farmer")
            new_state.move_to_right(item)
            print("farmer and ", item, " move from left to right")
            return new_state
        elif state.right_bank["farmer"] == 1 and state.right_bank[item] == 1:
            new_state.path.append(state)
            new_state.move_to_left("farmer")
            new_state.move_to_left(item)
            print("farmer and ", item, " move from right to left")
            return new_state
        else:
            print("Farmer and ", item, " are on opposite banks")
            return None

    def populate_frontier(self):  # STUDENT SOLUTION
        names = ["farmer", "wolf", "goat", "cabbage"]
        for x in range(0, 4):
            print(names[x])
            new_state = deepcopy(self.next_state(self.state, names[x]))
            if new_state != ValueError:
                self.frontier.append(new_state)


    class RiverCrossingState:
        def __init__(self, left, right):
            self.left_bank = left.copy()  # dictionary of thing:num
            self.right_bank = right.copy()  # dictionary of thing:num
            self.path = []

        def __eq__(self, other):
            """Overrides the default implementation"""
            if isinstance(other, RiverCrossingProblem.RiverCrossingState):
                return self.left_bank == other.left_bank and self.right_bank == other.right_bank
            return False

        def __repr__(self):
            return f'RiverCrossingState: \nleft bank: {self.left_bank} \nright bank: {self.right_bank}\n'

        def can_move(self, item):
            return (item == "farmer") or \
                   (self.right_bank.get(item, 0) > 0 and self.right_bank.get("farmer", 0) > 0) or \
                   (self.left_bank.get(item, 0) > 0 and self.left_bank.get("farmer", 0) > 0)

        def move_to_right(self, item):
            if self.left_bank.get(item, 0) > 0:
                self.left_bank[item] -= 1
            else:
                raise ValueError
            if item in self.right_bank:
                self.right_bank[item] += 1
            else:
                self.right_bank[item] = 1

        def move_to_left(self, item):
            if self.right_bank.get(item, 0) > 0:
                self.right_bank[item] -= 1
            else:
                raise ValueError
            if item in self.left_bank:
                self.left_bank[item] += 1
            else:
                self.left_bank[item] = 1

        def is_valid_state(self):  # STUDENT SOLUTION
            
            #TODO
            if self.left_bank["farmer"] == 0 and self.left_bank["wolf"] == 1 and self.left_bank["goat"] == 1:
                return False
            if (self.left_bank["farmer"] == 0) and (self.left_bank["goat"] == 1) and (self.left_bank["cabbage"] == 1):
                return False
            if (self.right_bank["farmer"] == 0) and (self.right_bank["wolf"] == 1) and (self.right_bank["goat"] == 1):
                return False
            if (self.right_bank["farmer"] == 0) and (self.right_bank["goat"] == 1) and (self.right_bank["cabbage"] == 1):
                return False
            else:
                return True


           
