#!/usr/bin/python3
""" Create validUTF8 function """


def validUTF8(data):
    """ check if valid UTF8 """
    flag = 0
    for i in data:
        if i > 255 or i < 0:
            continue

        if type(i) is not int:
            return False

        binary_number = bin(i).replace('0b', '').rjust(8, '0')[-8:]

        count_1 = 0

        for num in binary_number:
            if num != '1':
                break
            count_1 += 1

        if flag > 0:
            flag -= 1
            if count_1 != 1:
                return False
        else:
            if count_1 == 0:
                continue
            elif count_1 == 1 or count_1 > 4:
                return False
            else:
                flag = count_1 - 1
    return flag == 0
