#!/usr/bin/python3
"""Check if lists of integers is a valid utf-8"""


def validUTF8(data):
    i = 0
    while i < len(data):
        byte = data[i]

        # Get the number of bytes for the current character
        if byte & 0b10000000 == 0:  # 1-byte character
            num_bytes = 1
        elif byte & 0b11100000 == 0b11000000:  # 2-byte character
            num_bytes = 2
        elif byte & 0b11110000 == 0b11100000:  # 3-byte character
            num_bytes = 3
        elif byte & 0b11111000 == 0b11110000:  # 4-byte character
            num_bytes = 4
        else:
            return False

        # Check continuation bytes
        for j in range(1, num_bytes):
            if i + j >= len(data) or (data[i + j] & 0b11000000) != 0b10000000:
                return False

        # Move to the next character
        i += num_bytes

    return True
