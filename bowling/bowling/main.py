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



def add_game():
    bowler = input("Bowler's name: ").lower()
    utcdate = input("Date of Game: ")
    game = input("Which game is this: ")
    f1b1 = input("How many pins first ball frame 1: ")
    if int(f1b1) not 10:
        split = input("Was there a split: ")
        if split.lower == "yes"
            f1s = input("which pins were left: ie. 6,7,10 ")
        f1b2 = input("How many pins second ball frame 1: ")



if __name__ == "__main__":
    main()
