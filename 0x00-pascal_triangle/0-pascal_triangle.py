#!/usr/bin/python3


def pascal_triangle(n):
    """ return the pascal triangle as list of lists """
    mylist = []
    if n <= 0:
        return mylist
    for i in range(n):
        tmp = []
        for j in range(i + 1):
            if i == 0:
                mylist.append([1])
            else:
                if j == 0:
                    tmp.append(1)
                elif j == i:
                    tmp.append(1)
                    mylist.append(tmp)
                else:
                    x = mylist[i - 1][j - 1]
                    y = mylist[i - 1][j]
                    tmp.append(x + y)
    return mylist
