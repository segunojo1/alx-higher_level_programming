#!/usr/bin/python3
"""  list all states based on the first name  """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    value = sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s "
                "ORDER BY states.id",
                (value, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
