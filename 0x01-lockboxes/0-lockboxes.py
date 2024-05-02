#!/usr/bin/python3
""" Implement the lockboxes task as interview """


def canUnlockAll(boxes):
    def dfs(box_index):
        visited.add(box_index)
        for key in boxes[box_index]:
            if key not in visited:
                dfs(key)

    visited = set()
    dfs(0)
    return len(visited) == len(boxes)
