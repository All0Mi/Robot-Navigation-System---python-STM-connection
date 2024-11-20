import heapq
import numpy as np

def heuristic(a, b):
    """
    Manhattan distance heuristic for A*.
    
    :param a: Current position as a tuple (x, y).
    :param b: Goal position as a tuple (x, y).
    :return: Manhattan distance between points a and b.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    """
    A* algorithm for 2D grid pathfinding.
    
    :param grid: 2D numpy array where 0 is free space, and 1 is an obstacle.
    :param start: Starting position as a tuple (x, y).
    :param goal: Goal position as a tuple (x, y).
    :return: List of tuples representing the path from start to goal.
    """
    rows, cols = grid.shape
    open_set = []
    heapq.heappush(open_set, (0, start, []))  # (cost, position, path)
    visited = set()

    while open_set:
        cost, current, path = heapq.heappop(open_set)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path + [goal]

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # N, S, W, E
            neighbor = (current[0] + dr, current[1] + dc)

            # Check if neighbor is valid and not an obstacle
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0], neighbor[1]] == 0:
                new_cost = cost + 1 + heuristic(neighbor, goal)
                heapq.heappush(open_set, (new_cost, neighbor, path + [current]))

    return []  # No path found
