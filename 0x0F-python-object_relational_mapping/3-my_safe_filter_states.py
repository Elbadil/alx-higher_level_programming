#!/usr/bin/python3
"""MySQLdb Module that connects Python script to a database"""


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
    safe_rgv_states = "SELECT * FROM states WHERE name LIKE BINARY %s"
    cursor.execute(safe_rgv_states, (argv[4],))
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    conn.close()
