from .connection import Cursor
from mysql.connector import Error


def database_use(database_name):
    cursor = Cursor().cursor
    try:
        cursor.execute(f"USE {database_name}")
        return f"USE {database_name}: OK"
    except Error as err:
        return f"USE {database_name}: {err.msg}"