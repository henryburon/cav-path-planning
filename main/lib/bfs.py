"""This module contains the implementation of the Breadth-First Search algorithm.
The algorithm is implemented as a function that takes a map, a start point and a goal point as input and returns the path from the start to the goal.
The algorithm is visualized using matplotlib FuncAnimation.
The module also contains a function to request the start and goal points from the user.
The module is used in main.py to find the path from the start to the goal and visualize the path using matplotlib FuncAnimation.

Returns:
    None
"""
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from collections import deque

def bfs(map, start, goal):
    """this function implements the Breadth-First Search algorithm to find the path from the start to the goal in the map.

    Args:
        map (): the  map as a numpy array
        start (): the start point
        goal (): the goal point

    Returns:
        None
    """
    queue = deque([start])
    visited = set([start])
    came_from = {}

    while queue:
        current = queue.popleft()

        if current == goal:
            return reconstruct_path(goal, came_from)

        for neighbor in get_neighbors(current, map):
            if map[neighbor[0]][neighbor[1]] != 255 and neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)

    return None

def get_neighbors(cell, map):
    """this function returns the valid neighbors of a cell in the map

    Args:
        cell (): the cells in the map
        map (): the map as a numpy array

    Returns:
        neighbors: the valid neighbors of a cell in the map
    """
    # Returns the valid neighbors of a cell in the map
    neighbors = [(cell[0] + dx, cell[1] + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
    return [(x, y) for x, y in neighbors if 0 <= x < len(map) and 0 <= y < len(map[0])]

def reconstruct_path(goal, came_from):
    """
    This function reconstructs the path from the goal to the start using the came_from dictionary.
    It starts from the goal and works its way back to the start by looking up the previous node in the path until it reaches the start.
    The path is then reversed to get the path from start to goal.
    """
    # Reconstruct the path from the goal to the start
    path = [goal]
    while goal in came_from:
        goal = came_from[goal]
        path.append(goal)
    path.reverse()
    return path

def update_bfs(frame, path_lines, path, start, goal, map):
    """This function updates the visualization of the BFS algorithm.

    Args:
        frame (): the current frame
        path_lines (): the lines representing the path
        path (): the path taken by the algorithm
        start (): the start coordinate
        goal (): the end coordinate
        map (): the map as a numpy array

    Returns:
        path_lines: lines representing the path
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
    """This function requests the start and goal points from the user by displaying the map and waiting for the user to click two points.

    Args:
        map (): the map
        xplot (): the width of the plot
        yplot (): the height of the plot

    Returns:
        start: the start point
        goal: the goal point
    """
    fig = plt.figure(figsize=(xplot, yplot))
    plt.imshow(map, cmap='Greys', interpolation='nearest')
    plt.title("Select the start and goal points (click 2 points)", fontsize=15, fontweight='bold', color='purple')
    start, goal = plt.ginput(2, timeout=-1)
    start = (int(start[1]), int(start[0]))
    goal = (int(goal[1]), int(goal[0]))
    plt.close()
    return start, goal
