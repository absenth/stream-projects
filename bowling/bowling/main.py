import sqlite3
from datetime import datetime


from db_utils import(
        db_connect,
        db_create,
        db_check)


con = db_connect()
cur = con.cursor()


def main():
    if not db_check():
        db_create()
    else:
        print("DB Already Exists")


if __name__ == "__main__":
    main()
