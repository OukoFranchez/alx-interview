#!/usr/bin/env python3
""" Task 0 Module """


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
Return the start and end indices for a given page and page size.

Parameters:
- page (int): The page number.
- page_size (int): The number of items per page.

Returns:
- tuple[int, int]: A tuple containing the start and end indices
for the given page.
"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
