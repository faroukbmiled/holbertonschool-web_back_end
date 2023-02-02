import re
from typing import List
"""filter_datum"""


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """filter_datum"""
    for field in fields:
        message = re.sub(fr'{field}=.+?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message.rstrip(separator)
