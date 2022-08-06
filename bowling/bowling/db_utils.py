#!/usr/bin/env python3

import sqlite3


dbname = "bowling"


def db_connect():
    con = sqlite3.connect(dbname)
    return con


con = db_connect()
cur = con.cursor()


def db_create():
    cur.execute('''CREATE TABLE IF NOT EXISTS stats
        ([key] INTEGER PRIMARY KEY NOT NULL, [bowler] TEXT NOT NULL,
        [utcdate] TEXT NOT NULL, [game] INTEGER NOT NULL,
        [f1b1] INTEGER NOT NULL,  [f1b2] INTEGER,  [f1s] TEXT
        [f2b1] INTEGER NOT NULL,  [f2b2] INTEGER,  [f2s] TEXT
        [f3b1] INTEGER NOT NULL,  [f3b2] INTEGER,  [f3s] TEXT
        [f4b1] INTEGER NOT NULL,  [f4b2] INTEGER,  [f4s] TEXT
        [f5b1] INTEGER NOT NULL,  [f5b2] INTEGER,  [f5s] TEXT
        [f6b1] INTEGER NOT NULL,  [f6b2] INTEGER,  [f6s] TEXT
        [f7b1] INTEGER NOT NULL,  [f7b2] INTEGER,  [f7s] TEXT
        [f8b1] INTEGER NOT NULL,  [f8b2] INTEGER,  [f8s] TEXT
        [f9b1] INTEGER NOT NULL,  [f9b2] INTEGER,  [f9s] TEXT
        [f10b1] INTEGER NOT NULL, [f10b2] INTEGER, [f10b3], INTEGER [f10s] TEXT
        )''')

    return True


def db_check():
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    return(cur.fetchall())


if __name__ == "__main__":
    db_check()
