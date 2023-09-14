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

    cities_of_states = """SELECT c.name
                          FROM states s
                          JOIN cities c
                          ON s.id = c.state_id
                          WHERE s.name = %s
                          ORDER BY c.id"""

    cursor.execute(cities_of_states, (argv[4],))
    results = cursor.fetchall()

    city_names = [row[0] for row in results]
    concat_city_names = ", ".join(city_names)
    print(concat_city_names)

    cursor.close()
    conn.close()
