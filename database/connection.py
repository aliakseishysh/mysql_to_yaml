from contextlib import contextmanager
from enviroment.enviroment import credentials_get
import mysql.connector as connector
from utils.singleton import Singleton
import yaml


class Connection(metaclass=Singleton):

    def __init__(self):
        self.DB_USER, self.DB_PASSWORD, self.DB_HOST = credentials_get()
        self.connection = connector.connect(user=self.DB_USER, 
                                            password=self.DB_PASSWORD, 
                                            host=self.DB_HOST)

    def __enter__(self):
        yield self.connection

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()
        del self


class Cursor(metaclass=Singleton):

    def __init__(self):
        self.cursor = Connection().connection.cursor(buffered=True)

    def __enter__(self):
        yield self.cursor

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.cursor.close()
        del self

