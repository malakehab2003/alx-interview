#!/usr/bin/python3
""" solve the log parsing task """
import sys

def parse_line(line):
    """Parse a line of input and extract file size and status code."""
    parts = line.split()
    if len(parts) == 9 and parts[4] == '"GET':
        try:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            return file_size, status_code
        except ValueError:
            pass
    return None, None

def print_status(total_size):
    """Print total file size and status codes."""
    print('File size:', total_size)
    for key in sorted(status_dict.keys()):
        value = status_dict[key]
        if value > 0:
            print('{}: {}'.format(key, value))
            status_dict[key] = 0

total_size = 0
count = 0
status_dict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line in sys.stdin:
        size, status = parse_line(line)
        if size is not None and status is not None:
            total_size += size
            status_dict[status] += 1
        count += 1
        if count == 10:
            print_status(total_size)
            total_size = 0
            count = 0
except KeyboardInterrupt:
    print_status(total_size)
    sys.exit(0)
