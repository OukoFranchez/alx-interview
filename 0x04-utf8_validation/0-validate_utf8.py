#!/usr/bin/python3
""" validUTF8 Module """


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
    - data: A list of integers representing bytes of data.

    Returns:
    - True if data is a valid UTF-8 encoding, else returns False.
    """
    # Number of bytes to follow for each leading byte in UTF-8
    num_bytes_to_follow = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}

    # Iterate through each byte in the data
    i = 0
    while i < len(data):
        leading_byte = data[i]

        # If the leading byte is within the range of a
        # single-byte character, move to next byte
        if leading_byte >> 7 == 0:
            i += 1
            continue

        # Determine the number of bytes to follow based on the leading byte
        num_following_bytes = num_bytes_to_follow.get(leading_byte >> 4, -1)
        if num_following_bytes == -1:
            return False

        # Check if there are enough following bytes in the data
        if i + num_following_bytes >= len(data):
            return False

        # Check following bytes
        for j in range(1, num_following_bytes + 1):
            if data[i + j] >> 6 != 0b10:
                return False

        # Move to next character
        i += num_following_bytes + 1

    return True
