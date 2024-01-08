#!/usr/bin/python3


def validUTF8(data):
    '''a method that determines if a given data set
    represents a valid UTF-8 encoding'''
    remaining_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        mask = 1 << 7
        if remaining_bytes == 0:
            while mask & num:
                remaining_bytes += 1
                mask = mask >> 1

            if remaining_bytes == 0:
                continue
            if remaining_bytes == 1 or remaining_bytes > 4:
                return False

        else:
            if not (num & mask1 and not (num & mask2)):
                return False

        remaining_bytes -= 1
    return remaining_bytes == 0
