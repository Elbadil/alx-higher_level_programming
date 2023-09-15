#!/usr/bin/python3
"""MySQLdb Module that connects Python script to a database """


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = conn.cursor()
    n_states = """SELECT * FROM states
                  WHERE name LIKE BINARY 'N%'
                  ORDER BY states.id ASC"""

    cursor.execute(n_states)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    conn.close()
