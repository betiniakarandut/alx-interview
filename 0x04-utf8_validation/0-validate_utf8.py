#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ Checks whether a given list is utf-8 valid
    Args:
        data (list): list of integers
    Returns:
        bool: True data is valid else False
    """
    check_byte = 0
    for any_byte in data:
        mask = 1 << 7
        if not check_byte:
            while mask & any_byte:
                check_byte += 1
                mask >>= 1
            if not check_byte:
                continue
            if check_byte == 1 or any_byte > 4:
                return False
        else:
            if any_byte >> 6 != 2:
                return False
        check_byte -= 1
    return True
