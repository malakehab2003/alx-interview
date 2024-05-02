#!/usr/bin/python3
""" Implement the lockboxes task as interview """


def canUnlockAll(boxes):
    """ Implement can unlock All for lock boxes problem """
    mySet = set()
    newSet = set()
    newSet.update(boxes[0])
    for i in range(len(boxes)):
        mySet = mySet.union(newSet)
        newSet = itterateSet(newSet, boxes)
    print(mySet)



def itterateSet(mySet, boxes):
    """ Itterate over a set """
    newSet = set()
    for i in mySet:
        newSet.update(boxes[i])
    return newSet
