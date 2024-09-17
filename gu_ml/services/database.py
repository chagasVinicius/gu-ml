from abc import ABC, abstractmethod  # new
import psycopg
import os

from psycopg.rows import dict_row


class Database(ABC):
    """
    Database context manager
    """

    def __init__(self, driver) -> None:
        self.driver = driver

    @abstractmethod
    def connect_to_database(self):
        raise NotImplementedError()

    def __enter__(self):
        self.connection = self.connect_to_database()
        self.cursor = self.connection.cursor(row_factory=dict_row)
        return self

    def __exit__(self, exception_type, exc_val, traceback):
        self.cursor.close()
        self.connection.close()


class PgDatabase(Database):
    """PostgreSQL Database context manager"""

    def __init__(self) -> None:
        self.driver = psycopg
        super().__init__(self.driver)

    def connect_to_database(self):
        return self.driver.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PWD"),
            dbname=os.getenv("DB_NAME"),
        )
