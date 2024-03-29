"""this module contains the astar algorithm and the visualization of the path

Returns:
    None
"""
import heapq
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def astar(map, start, goal, heuristic):
    """This function implements the A* algorithm to find the path from the start to the goal in the map.

    Args:
        map (): the map as a numpy array
        start (): the start point
        goal (): the goal point
        heuristic (): the manhattan distance between the each cell and the goal

    Returns:
        None
    """
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
            if map[neighbor[0]][neighbor[1]] != 255 and neighbor not in closed_set:
                tentative_g_score = g_score[current] + 1  # The cost from current to neighbor is 1

                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return None

def initialize_came_from():
    """This function initializes the came_from dictionary.

    Returns:
        came_from: the dictionary to store the parent of each cell
    """
    # Create a dictionary to store the parent of each cell
    came_from = {}
    return came_from

def get_neighbors(cell, map):
    """This function returns the valid neighbors of a cell in the map

    Args:
        cell (): the cells in the map
        map (): the map as a numpy array

    Returns:
        neighbors: the valid neighbors of a cell in the map
    """
    # Returns the valid neighbors of a cell in the map
    neighbors = [(cell[0] + dx, cell[1] + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
    return [(x, y) for x, y in neighbors if 0 <= x < len(map) and 0 <= y < len(map[0])]

def heuristic(cell, goal):
    """This function calculates the manhattan distance between the each cell and the goal

    Args:
        cell (): the cells in the map
        goal (): the goal point

    Returns:
        distance: the manhattan distance between the each cell and the goal
    """
    # Calculate the manhattan distance between the each cell and the goal
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

def reconstruct_path(goal, came_from):
    """This function reconstructs the path from the goal to the start using the came_from dictionary.

    Args:
        goal (): the goal point
        came_from (): the dictionary to store the parent of each cell

    Returns:
        path: the path from the start to the goal
    """
    # Reconstruct the path from the goal to the start
    path = [goal]
    while goal in came_from:
        goal = came_from[goal]
        path.append(goal)
    path.reverse()
    return path

def update(frame, path_lines, path, start, goal, map):
    """This function updates the visualization of the A* algorithm.

    Args:
        frame (): the current frame
        path_lines (): the path lines
        path (): the path from the start to the goal
        start (): the start point
        goal (): the goal point
        map (): the map as a numpy array

    Returns:
        path_lines: the path lines
    """
    plt.clf()
    plt.imshow(map, cmap='Greys', interpolation='nearest')

    # Plot the path points up to the current frame
    path_x, path_y = zip(*path[:frame + 1])
    plt.plot(path_y, path_x, marker='x', color='red', markersize=2)
    plt.plot(start[1], start[0], marker='o', color='green', markersize=5)
    plt.plot(goal[1], goal[0], marker='o', color='blue', markersize=5)

    # Plot the lines between path points
    for i in range(frame):
        plt.plot([path[i][1], path[i + 1][1]], [path[i][0], path[i + 1][0]], color='red')

    path_lines.set_data(path_y, path_x)
    return path_lines

def request_start_and_goal(map, xplot, yplot):
    """This function requests the start and goal points from the user.

    Args:
        map (): the map as a numpy array
        xplot (): the width of the plot
        yplot (): the height of the plot

    Returns:
        start: the start point
        goal: the goal point
    """
    fig = plt.figure(figsize=(xplot, yplot))
    plt.imshow(map, cmap='Greys', interpolation='nearest')
    plt.title("Select the start and goal points (click 2 points)", fontsize=15, fontweight='bold', color='red')
    start, goal = plt.ginput(2, timeout=-1)
    start = (int(start[1]), int(start[0]))
    goal = (int(goal[1]), int(goal[0]))
    plt.close()
    return start, goal

