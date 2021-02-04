#!/usr/bin/env python3

from abc import ABC
from logging import error
import sqlite3
from lib.base import BaseDrinkClass


class Formulate(ABC):
    @staticmethod
    def query():
        pass

class FormulateInsert(Formulate):
    """
    Insert data in to data
    """
    @staticmethod
    def query(table: str, columns: tuple, values: tuple):
        return f"INSERT INTO {table} {columns}\
            VALUES {values};"


class FormulateDeleteEntry(Formulate):
    @staticmethod
    def query(table, id):
        return f"DELETE FROM {table} WHERE id = {id};"


class FormulateViewQuery(Formulate):
    @staticmethod
    def query(table: str):
        return f"SELECT * FROM {table};"

class FormulatesViewColumns(Formulate):
    @staticmethod
    def query(table):
        return f"PRAGMA table_info({table});"

class FormulateDropTable(Formulate):
    @staticmethod
    def query(table: str):
        return f"DROP TABLE {table};"


class FormulateShowTables(Formulate):
    @staticmethod
    def query():
        return "SELECT name FROM sqlite_master WHERE type='table';"

class Accessor(BaseDrinkClass):

    def __init__(self, database=None) -> None:
        super().__init__()
        self.database = database
        self.conn = self.connect()

    def connect(self):
        self.debug("Attempting to connect")
        try:
            conn = sqlite3.connect(self.database)
            return conn
        except sqlite3.Error as E:
            self.error(E)

    def execute(self, sql):
        try:
            cursor = self.conn.cursor()
            self.info(f"Attempting to execute {sql}")
            cursor.execute(sql)
            if "INSERT" or "DELETE" or "CREATE" in sql:
                self.conn.commit()
            return cursor.fetchall()
        except sqlite3.Error as err:
            self.exception(err)
            self.close()

    def close(self):
        self.conn.close()