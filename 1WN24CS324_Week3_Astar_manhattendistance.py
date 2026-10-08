import heapq

class PuzzleNode:
    def __init__(self, state, g=0, h=0, parent=None):
        self.state = state
        self.g = g  # Depth / Path cost
        self.h = h  # Heuristic cost (Manhattan Distance)
        self.f = g + h
        self.parent = parent

   
    def __lt__(self, other):
        return self.f < other.f


def calculate_manhattan_distance(state, goal_state):
    """Calculates total Manhattan Distance |x1 - x2| + |y1 - y2| for all tiles (excluding 0)."""
    distance = 0
    

    goal_positions = {goal_state[i]: (i // 3, i % 3) for i in range(9)}

    for i in range(9):
        tile = state[i]
        if tile != 0: 
            current_row, current_col = i // 3, i % 3
            target_row, target_col = goal_positions[tile]
            
            distance += abs(current_row - target_row) + abs(current_col - target_col)

    return distance


def get_neighbors(state):
    """Generates next valid states by sliding the blank tile (0)."""
    neighbors = []
    zero_idx = state.index(0)
    row, col = zero_idx // 3, zero_idx % 3

 
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero_idx = new_row * 3 + new_col
          
            new_state = list(state)
            new_state[zero_idx], new_state[new_zero_idx] = new_state[new_zero_idx], new_state[zero_idx]
            neighbors.append(tuple(new_state))

    return neighbors


def a_star_manhattan_distance(initial_state, goal_state):
    """A* Search implementation using Manhattan Distance heuristic."""
    start_h = calculate_manhattan_distance(initial_state, goal_state)
    start_node = PuzzleNode(initial_state, g=0, h=start_h)

    open_set = []
    heapq.heappush(open_set, start_node)
    

    g_costs = {initial_state: 0}

    while open_set:
        current_node = heapq.heappop(open_set)

        # Goal Check
        if current_node.state == goal_state:
            path = []
            curr = current_node
            while curr:
                path.append(curr)
                curr = curr.parent
            return path[::-1]  # Return path from start to goal

    
        for neighbor_state in get_neighbors(current_node.state):
            tentative_g = current_node.g + 1

            if neighbor_state not in g_costs or tentative_g < g_costs[neighbor_state]:
                g_costs[neighbor_state] = tentative_g
                h_cost = calculate_manhattan_distance(neighbor_state, goal_state)
                neighbor_node = PuzzleNode(neighbor_state, g=tentative_g, h=h_cost, parent=current_node)
                heapq.heappush(open_set, neighbor_node)

    return None


def print_board(state):
    """Displays 3x3 board cleanly."""
    for i in range(0, 9, 3):
        print(f"{state[i]} {state[i+1]} {state[i+2]}")
    print()



if __name__ == "__main__":
  
    initial_state = (1, 2, 3, 
                     0, 4, 6, 
                     7, 5, 8)

    goal_state = (1, 2, 3, 
                  4, 5, 6, 
                  7, 8, 0)

    solution_path = a_star_manhattan_distance(initial_state, goal_state)

    if solution_path:
        print(f"Solution found in {len(solution_path) - 1} steps:\n")
        for step, node in enumerate(solution_path):
            print(f"--- Step {step} (g={node.g}, h={node.h}, f={node.f}) ---")
            print_board(node.state)
    else:
        print("No solution found.")