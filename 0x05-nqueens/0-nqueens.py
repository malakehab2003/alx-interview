#!/usr/bin/python3
""" solve n queen problem """
import sys


# check the number of args
if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

# check that the second arg is a number
try:
    n = int(sys.argv[1])
except Exception:
    print("N must be a number")
    sys.exit(1)

# check if number smaller than 4
if n > 4:
    print('N must be at least 4')
    sys.exit(1)

# check col and positive and negative diagonal
cols = []
pos_diagonal = []
neg_diagonal = []


# search for all possible solutions
my_list = []
i = 0
col = 0

def remove_old_data(i):
    """
    remove data of the queen which aready moved
    """
    remove_item = []

    # get the item to remove
    for sublist in my_list:
        if sublist and sublist[0] == i:
            remove_item.append(sublist)

    # remove item from my_list
    for item in remove_item:
        my_list.remove(item)

    # remove item from neg_diagonal, pos_diagonal and cols
    row, col = remove_item[0][:2]
    pos_diagonal.remove(row - col)
    neg_diagonal.remove(row + col)
    cols.remove(col)
    return col


while i < n:
    while col in range(n):
        # if the place don't have any problem
        # with positive and negative diagonal and columns place it
        if (col not in cols and
                (i - col) not in pos_diagonal and
                (i + col) not in neg_diagonal):
            cols.append(col)
            pos_diagonal.append(i - col)
            neg_diagonal.append(i + col)
            my_list.append([i, col])
            if i == n - 1:
                break
            i += 1
            col = 0
        elif col == n - 1:
            # if we reached to the end of the row and can't add the queen
            # we return to the last added queen and move it to the next place
            # and modify cols, neg_diagonal and pos_diagonal
            i -= 1
            col = remove_old_data(i)
            if col < n - 1:
                col += 1
            else:
                i-= 1
                col = remove_old_data(i) + 1

        else:
            col += 1
    if len(my_list) == n:
        print(my_list)
        i = 0
        col = cols[0] + 1
        if col == n - 1:
            break
        cols.clear()
        my_list.clear()
        pos_diagonal.clear()
        neg_diagonal.clear()

