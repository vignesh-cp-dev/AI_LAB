import heapq

class PuzzleState:
    def __init__(self, board, parent=None, move="", depth=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth  # g(n)
        self.h = self.calculate_misplaced_tiles()  # h(n)
        self.f = self.depth + self.h  # f(n) = g(n) + h(n)

    def __lt__(self, other):
        return self.f < other.f

    def calculate_misplaced_tiles(self):
        goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        misplaced = 0
        for i in range(9):
           
            if self.board[i] != 0 and self.board[i] != goal[i]:
                misplaced += 1
        return misplaced

    def get_zero_index(self):
        return self.board.index(0)

    def get_neighbors(self):
        neighbors = []
        zero_idx = self.get_zero_index()
        row, col = zero_idx // 3, zero_idx % 3
        
        moves = {
            "Up": (-1, 0),
            "Down": (1, 0),
            "Left": (0, -1),
            "Right": (0, 1)
        }

        for move, (dr, dc) in moves.items():
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_zero_idx = new_row * 3 + new_col
                new_board = list(self.board)
                
                new_board[zero_idx], new_board[new_zero_idx] = new_board[new_zero_idx], new_board[zero_idx]
                neighbors.append(PuzzleState(tuple(new_board), self, move, self.depth + 1))
        return neighbors

def solve_a_star(start_board):
    start_state = PuzzleState(tuple(start_board))
    goal_board = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    
    open_list = []
    heapq.heappush(open_list, start_state)
    closed_set = set()

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.board == goal_board:
            path = []
            state = current_state
            while state.parent:
                path.append((state.move, state.board))
                state = state.parent
            path.reverse()
            return path, current_state.depth

        closed_set.add(current_state.board)

        for neighbor in current_state.get_neighbors():
            if neighbor.board in closed_set:
                continue
            heapq.heappush(open_list, neighbor)
            
    return None, -1


initial_board = [
    1, 2, 3,
    0, 4, 6,
    7, 5, 8
]

print("Initial State:")
for i in range(0, 9, 3):
    print(initial_board[i:i+3])

solution_path, total_depth = solve_a_star(initial_board)

if solution_path:
    print(f"\nSolved in {total_depth} steps (g(n) = {total_depth}):")
    for step, (move, board) in enumerate(solution_path, 1):
        print(f"Step {step} - Move {move}:")
        for i in range(0, 9, 3):
            print(list(board)[i:i+3])
else:
    print("No solution found.")