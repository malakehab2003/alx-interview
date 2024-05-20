#!/usr/bin/env python3
""" solve the log parsing task """
import sys


def parse_line(line):
    """ parse the line """
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
        return size, str(status)
    return None, None


if __name__ == '__main__':
    total_size = 0
    count = 0
    status_dict = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }


    def print_status(total_size):
        print('File size: {:d}'.format(total_size))
        for key in sorted(status_dict.keys()):
            value = status_dict[key]
            if value == 0:
                continue
            print('{:s}: {:d}'.format(key, value))

    try:
        for line in sys.stdin:
            size, status = parse_line(line)
            count += 1
            if total_size is not None and status is not None:
                total_size += size
                status_dict[status] += 1

            if count == 10:
                print_status(total_size)
                count = 0
    except (KeyboardInterrupt, EOFError):
        print_status(total_size)
