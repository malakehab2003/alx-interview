#!/usr/bin/python3
""" Create validUTF8 function """


def validUTF8(data):
    """Check if valid UTF-8"""
    remaining_bytes = 0
    for i in data:
        if i > 255:
            return False

        binary_number = bin(i)[2:].rjust(8, '0')

        # For the first byte
        if remaining_bytes == 0:
            # Count the number of leading 1s to determine the length of the UTF-8 character
            for bit in binary_number:
                if bit == '0':
                    break
                remaining_bytes += 1

            # If this is a 1-byte character (no leading 1s)
            if remaining_bytes == 0:
                continue

            # If remaining_bytes is 1 or greater than 4, it's an invalid character
            if remaining_bytes == 1 or remaining_bytes > 4:
                return False

        else:  # For continuation bytes
            # Check that the byte is a valid continuation byte (starts with 10)
            if not (binary_number.startswith('10') and remaining_bytes > 0):
                return False

            remaining_bytes -= 1

    # All characters should be fully parsed, and no remaining bytes should be expected
    return remaining_bytes == 0
