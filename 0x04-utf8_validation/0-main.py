#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('test').validUTF8

# Test cases with their expected answers
test_cases = [
    # Single-byte characters
    ([65], True),          # ASCII character 'A'
    ([97], True),          # ASCII character 'a'
    ([240], False),        # Invalid: 11110000 (overlong encoding)

    # Two-byte characters
    ([195, 128], True),    # UTF-8 encoding of U+0080 (€)
    ([197, 151], True),    # UTF-8 encoding of U+0097 (‘)
    ([192, 191], False),   # Invalid: 11000000 10111111 (overlong encoding)

    # Three-byte characters
    ([226, 130, 172], True),   # UTF-8 encoding of U+20AC (€)
    ([224, 160, 128], True),   # UTF-8 encoding of U+0800 (ࠀ)
    ([226, 130, 177], True),   # UTF-8 encoding of U+20B1 (₱)

    # Four-byte characters
    ([240, 144, 133, 152], True),   # UTF-8 encoding of U+10348 (𐍈)
    ([244, 143, 183, 191], False),  # Invalid: 11110100 10001111 10111111 10111111 (invalid leading byte)
    ([240, 144, 128], False),       # Invalid: Incomplete UTF-8 sequence

    # Mixed characters
    ([65, 226, 130, 172], True),    # ASCII 'A' + UTF-8 €
    ([195, 128, 226, 130, 177], True),  # UTF-8 € + UTF-8 ₱
]

# Testing each test case
for data, expected in test_cases:
    result = validUTF8(data)
    print(f"Input: {data} - Expected: {expected}, Result: {result}")
