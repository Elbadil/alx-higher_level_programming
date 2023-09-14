#!/usr/bin/python3
import MySQLdb
from sys import argv


if __name__ == "__main__":

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = conn.cursor()

    states_id = "SELECT * FROM states"
    cursor.execute(states_id)
    results = cursor.fetchall()

    for row in results:
        print(row)

    conn.close()
