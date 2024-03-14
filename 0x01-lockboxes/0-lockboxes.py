#!/usr/bin/python3
"""Lockboxes challenge"""


def canUnlockAll(boxes):
    '''
    Determines if all the boxes can be opened or not.

    Args:
        boxes (list): A list of lists representing boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    '''
    num_boxes = len(boxes)
    visited = set()  # Set to track visited boxes
    queue = [0]  # Start with box 0
    visited.add(0)  # Mark box 0 as visited

    while queue:
        current_box = queue.pop(0)  # Get the next box to explore
        for key in boxes[current_box]:
            if key < num_boxes and key not in visited:
                visited.add(key)  # Mark the box as visited
                queue.append(key)  # Add the box to the queue for exploration

    return len(visited) == num_boxes  # Check if all boxes have been visited
