from .connection import Cursor
from mysql.connector import Error


def select_all(table_name):
    try:
        cursor = Cursor().cursor
        cursor.execute(f"SELECT * FROM {table_name}")
        return f"SELECT * FROM {table_name}: OK"
    except Error as err:
        return f"SELECT * FROM {table_name}: {err.msg}"
