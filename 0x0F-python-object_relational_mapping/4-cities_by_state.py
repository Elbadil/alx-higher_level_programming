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

    cities_of_states = """SELECT c.id, c.name, s.name
                          FROM states s
                          JOIN cities c
                          ON s.id = c.state_id
                          ORDER BY c.id"""

    cursor.execute(cities_of_states)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    conn.close()
