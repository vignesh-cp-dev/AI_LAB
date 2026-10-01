class EightPuzzleDFS:
    def __init__(self, start_state, goal_state, max_depth=10):

        self.start_state = start_state
        self.goal_state = goal_state
        self.max_depth = max_depth

    def get_neighbors(self, state):
        neighbors = []
           row, col = -1, -1
        for r in range(3):
            for c in range(3):
                if state[r][c] == 0:
                    row, col = r, c
                    break

  
        moves = [
            (-1, 0, "UP"),
            (1, 0, "DOWN"),
            (0, -1, "LEFT"),
            (0, 1, "RIGHT")
        ]

        for dr, dc, move_name in moves:
            new_r, new_c = row + dr, col + dc
            if 0 <= new_r < 3 and 0 <= new_c < 3:
          
                new_board = [list(r) for r in state]
            
                new_board[row][col], new_board[new_r][new_c] = new_board[new_r][new_c], new_board[row][col]

                neighbors.append((tuple(tuple(r) for r in new_board), move_name))

        return neighbors

    def solve(self):
  
        stack = [(self.start_state, [], 0)]
        visited = set()

        while stack:
            state, path, depth = stack.pop()

            if state == self.goal_state:
                return path

            if state in visited:
                continue
            
            visited.add(state)

            if depth < self.max_depth:
              
                for neighbor_state, move in self.get_neighbors(state):
                    if neighbor_state not in visited:
                        stack.append((neighbor_state, path + [move], depth + 1))

        return None


start = (
    (1, 2, 3),
    (4, 0, 5),
    (7, 8, 6)
)

goal = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

solver = EightPuzzleDFS(start, goal, max_depth=5)
solution = solver.solve()

print("Moves to reach goal:", solution)
