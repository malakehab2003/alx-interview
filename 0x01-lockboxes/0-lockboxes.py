#!/usr/bin/python3
""" Implement the lockboxes task as interview """


def itterateSet(mySet, boxes, oldSet):
    """ Itterate over a set """
    newSet = set()
    for i in mySet:
        if i >= len(boxes) or i <= 0 or i in oldSet:
            continue
        newSet.update(boxes[i])
    return newSet


def canUnlockAll(boxes):
    """ Implement can unlock All for lock boxes problem """
    mySet = set()
    newSet = set()
    newSet.update(boxes[0])
    for i in range(len(boxes)):
        mySet = mySet.union(newSet)
        newSet = itterateSet(newSet, boxes, mySet - newSet)
    for i in range(len(boxes)):
        if i == 0:
            continue
        elif i not in mySet:
            return False
    return True
