#!/usr/bin/python3
"""
UTF-8 Validation Module
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
    - data: A list of integers representing bytes of data.

    Returns:
    - True if data is a valid UTF-8 encoding, else return False.
    """
    byte_count = 0  # Initialize byte count

    for i in data:  # Iterate through each integer in the data
        if byte_count == 0:  # If no continuation bytes expected
            # Determine the number of bytes expected for the current sequence
            if i >> 5 == 0b110 or i >> 4 == 0b1110 or i >> 3 == 0b11110:
                # Extract the number of bytes from the leading bits
                byte_count = i >> 3 & 0b11
                # Invalid number of bytes
                if byte_count == 0 or byte_count > 3:
                    return False
            # If the leading bit is not 0 for a single-byte character
            elif i >> 7 == 0b1:
                return False
        # If continuation bytes expected
        else:
            # Check if the current byte is a continuation byte
            if i >> 6 != 0b10:
                return False
            # Decrement byte count as a continuation byte is found
            byte_count -= 1
    # Return True if all bytes are validated, False otherwise
    return byte_count == 0
