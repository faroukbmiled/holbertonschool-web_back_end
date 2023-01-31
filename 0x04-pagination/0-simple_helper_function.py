#!/usr/bin/env python3
"""
index
"""


def index_range(page, page_size):
    """
    index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
