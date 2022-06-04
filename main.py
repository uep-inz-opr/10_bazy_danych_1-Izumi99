import sqlite3
import csv

if __name__ == '__main__':
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.execute("CREATE TABLE polaczenia (from_subscriber,to_subscriber,datetime,duration,celltower);")

    with open(input(), 'r') as file:
        dr = csv.DictReader(file, delimiter=";")
        to_db = [(i['from_subscriber'], i['to_subscriber'], i['datetime'], i['duration'], i['celltower']) for i in dr]

    cur.executemany("INSERT INTO polaczenia (from_subscriber,to_subscriber,datetime,duration,celltower) VALUES (?, ?, ?, ?, ?);", to_db)
    con.commit()

    cur.execute("SELECT SUM(duration) FROM polaczenia")
    print(cur.fetchall()[0][0])
    con.close()