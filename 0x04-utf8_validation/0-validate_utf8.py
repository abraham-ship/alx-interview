#!/usr/bin/python3


def validUTF8(data):
    '''a method that determines if a given data set
    represents a valid UTF-8 encoding'''
    remaining_bytes = 0

    for byte in data:
        if remaining_bytes == 0:
            if byte >> 3 == 0b11110:
                remaining_bytes = 3
            elif byte >> 4 == 0b1110:
                remaining_bytes = 2
            elif byte >> 5 == 0b110:
                remaining_bytes = 1
            elif byte >> 7 == 0:
                remaining_bytes = 0
            else:
                return False
        else:
            if byte >> 6 == 0b10:
                remaining_bytes -= 1
            else:
                return False

