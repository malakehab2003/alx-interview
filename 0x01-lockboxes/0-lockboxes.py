#!/usr/bin/python3
""" Implement the lockboxes task as interview """


def canUnlockAll(boxes):
    """ Create canUnlockAll to check if all boxes unlocked """
    mySet = {0}
    visited = set()

    while mySet:
        box = mySet.pop()
        visited.add(box)

        for key in boxes[box]:
            if key not in visited:
                mySet.add(key)

    return len(visited) == len(boxes)
