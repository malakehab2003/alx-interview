#!/usr/bin/python3
""" solve the log parsing task """
import sys


def parse_line(line):
    parse = line.split()
    if len(parse) == 9:
        try:
            size = int(parse[-1])
        except Exception:
            pass
        try:
            status = int(parse[-2])
        except Exception:
            pass
        return size, status
    return None, None

total_size = 0
count = 0
status_dict = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

for line in sys.stdin:
    size, status = parse_line(line)
    count += 1
    if total_size is not None and status is not None:
        total_size += size
        status_dict[status] += 1

    if count == 10:
        print('File size: {}'.format(total_size))
        for key, value in status_dict.items():
            if value == 0:
                continue
            print('{}: {}'.format(key, value))
        count = 0
        total_size = 0


    

