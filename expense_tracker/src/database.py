import sqlite3
from contextlib import contextmanager

import expense_tracker.src.constants as constants


@contextmanager
def connexion(path):
    connection = sqlite3.connect(path)
    try:
        yield connection
    except sqlite3.Error as error:
        print(f"{error.__class__.__name__}: {error}")
        raise
    else:
        connection.commit()
    finally:
        connection.close()


@contextmanager
def dbcursor():
    with connexion(constants.DB_FILE) as connection:
        cursor = connection.cursor()
        try:
            yield cursor
        finally:
            cursor.close()


def execute_(query):
    with dbcursor() as cursor:
        cursor.execute(query)


def fetch_all_records():
    with dbcursor() as cursor:
        cursor.execute("SELECT * FROM expenses;")
        return cursor.fetchall()


def create_table():
    create_expenses_table_query = """
                        CREATE TABLE IF NOT EXISTS expenses(
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          category TEXT NOT NULL,
                          amount REAL NOT NULL,
                          expense_date TEXT NOT NULL,
                          notes TEXT NOT NULL
                        );
                    """
    execute_(create_expenses_table_query)


def add_expense_entry():
    add_expense_query = """
    INSERT INTO
        expenses (category, amount, expense_date, notes)
    VALUES
        (?, ?, ?, ?),
        (category, amount, expense_date, note)
    """
    execute_(add_expense_query)
