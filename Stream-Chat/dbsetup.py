import sqlite3


dbname = "commandsdb"


def db_connect():
    con = sqlite3.connect(dbname)
    return con

con = db_connect()
cur = con.cursor()


def check_for_db():
    cur.execute("SELECT name from sqlite_master WHERE type='table'")
    return(cur.fetchall())


def setup_commands_db():
    cur.execute('''CREATE TABLE IF NOT EXISTS commands
        ([pk] INTEGER PRIMARY KEY NOT NULL,
        [command] TEXT, [commandout], TEXT''')

    return True


def insert_new_command(cur, newcommand):
    sql = '''INSERT INTO commands(command, commandout)
             VALUES(?, ?) '''
    cur.execute(sql, newcommand)
    con.commit()
    return cur.lastrowid


def add_command():
    new_command = input("What command would you like to add? ").lower()
    new_commandout = input("What should this command return? ")
    newcommand = (new_command, newcommandout)
    insert_new_command(con, newcommand)


def main():
    if not check_for_db():
        print("running setup_commands_db")
        setup_commands_db()



if __name__ == "__main__":
    main()
