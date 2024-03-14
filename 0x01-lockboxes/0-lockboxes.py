from collections import deque

def canUnlockAll(boxes):
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