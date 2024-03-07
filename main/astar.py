import heapq
import matplotlib.pyplot as plt

def astar(map, start, goal, heuristic):
    # Initialize the open set, closed set, g_score, and f_score
    open_set = [(heuristic(start, goal), start)]
    closed_set = set()
    g_score = {(x, y): float('inf') for x in range(len(map)) for y in range(len(map[0]))}
    f_score = {(x, y): float('inf') for x in range(len(map)) for y in range(len(map[0]))}
    g_score[start] = 0
    f_score[start] = heuristic(start, goal)
    came_from = {}  # Initialize came_from dictionary here

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            return reconstruct_path(goal, came_from)

        closed_set.add(current)

        for neighbor in get_neighbors(current, map):
            if map[neighbor[0]][neighbor[1]] != 100 and neighbor not in closed_set:
                tentative_g_score = g_score[current] + 1  # The cost from current to neighbor is 1

                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None


def initialize_came_from():
    # Create a dictionary to store the parent of each cell
    came_from = {}
    return came_from



def get_neighbors(cell, map):
    # Returns the valid neighbors of a cell in the map
    neighbors = [(cell[0] + dx, cell[1] + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
    return [(x, y) for x, y in neighbors if 0 <= x < len(map) and 0 <= y < len(map[0])]


def heuristic(cell, goal):
    # Calculate the manhattan distance between the each cell and the goal
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

def reconstruct_path(goal, came_from):
    # Reconstruct the path from the goal to the start
    path = [goal]
    while goal in came_from:
        goal = came_from[goal]
        path.append(goal)
    path.reverse()
    return path



def main():
    # Create a map
    map = [[1]*100 for _ in range(100)]

    # Add some obstacles
    for i in range(20, 40):
        for j in range(20, 40):
            map[i][j] = 100
    

    start = (1, 0)
    goal = (50, 20)

    # Find the path
    path = astar(map, start, goal, heuristic)

    if path is not None:
        # Print the path
        print(path)

        # Plot the path
        plt.imshow(map, cmap='Greys', interpolation='nearest')
        for cell in path:
            plt.text(cell[1], cell[0], 'x', ha='center', va='center', color='red')
        plt.xticks([]), plt.yticks([])
        plt.show()
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
