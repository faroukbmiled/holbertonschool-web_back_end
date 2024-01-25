#!/usr/bin/env python3
"""filter_datum"""
import logging
import re
from typing import List
import os
from mysql.connector import connection


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """init"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """filter_datum"""
    for field in fields:
        message = re.sub(fr'{field}=.+?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """get_logger"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


def get_db() -> connection.MySQLConnection:
    """get_db"""
    host = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    user = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    db_name = os.environ.get("PERSONAL_DATA_DB_NAME")

    if not db_name:
        raise Exception("PERSONAL_DATA_DB_NAME environment variable not set")

    cnx = connection.MySQLConnection(
                                        host=host,
                                        user=user,
                                        password=password,
                                        database=db_name,
                                        )

    return cnx


def main():
    """main func"""
    logger = get_logger()
    db = get_db()

    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")

    for row in cursor.fetchall():
        name, email, phone, ssn, password, ip, last_login, user_agent = row
        data = f"name={name}; email={email}; phone={phone}; ssn={ssn};\
            password={password}; ip={ip}; last_login={last_login};\
                user_agent={user_agent}"

        logger.info(data)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
