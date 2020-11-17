from .connection import Cursor
from mysql.connector import Error


def describe_table(table_name):
    try:
        cursor = Cursor().cursor
        cursor.execute(f"DESCRIBE {table_name}")
        return f"DESCRIBE {table_name}: OK"
    except Error as err:
        return f"DESCRIBE {table_name}: {err.msg}"