#!/usr/bin/python3
"""Lockboxes challenge"""


from collections import deque
def canUnlockAll(boxes):
    """
    Checks if all boxes in the given list of boxes can be unlocked.
    Parameters:
	- boxes (list): A list of lists representing the boxes. Each inner list contains the keys that can unlock the corresponding box.

	Returns:
	- bool: True if all boxes can be unlocked, False otherwise.

	Example:
	>>> boxes = [[1], [2], [3], []]
	>>> canUnlockAll(boxes)
	True

	>>> boxes = [[1, 2], [3], [], []]
	>>> canUnlockAll(boxes)
	False
	"""
    num_boxes = len(boxes)
    visited = set()  # Set to track visited boxes
    queue = deque([0])  # Start with box 0
    visited.add(0)  # Mark box 0 as visited

    while queue:
        current_box = queue.popleft()  # Get the next box to explore
        for key in boxes[current_box]:
            if key < num_boxes and key not in visited:
                visited.add(key)  # Mark the box as visited
                queue.append(key)  # Add the box to the queue for exploration

    return len(visited) == num_boxes  # Check if all boxes have been visited