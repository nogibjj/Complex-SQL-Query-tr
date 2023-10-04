"""
Design a complex SQL query 
involving joins, aggregation, and sorting
"""

import sqlite3
from mylib.query import log_query

LOG_FILE = "query_log.md"


def create_toy_db():
    conn = sqlite3.connect("toyDB.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS toyDB")
    c.execute('''
        CREATE TABLE IF NOT EXISTS toyDB (
            id INTEGER PRIMARY KEY,
            value INTEGER
        )
    ''')
    for i in range(1, 101):
        c.execute('INSERT INTO toyDB (id, value) VALUES (?, 1)', (i,))
    conn.commit()
    conn.close()
    return "toyDB.db"


def complex_query():
    """joins, aggregation, sorting"""
    
    # create a new toyDB
    create_toy_db()
    
    conn = sqlite3.connect("alcoholDB.db")
    c = conn.cursor()
    c.execute("ATTACH DATABASE 'toyDB.db' AS t")
    # join
    c.execute("""
        SELECT a.*, t.*
        FROM alcoholDB AS a
        INNER JOIN toyDB AS t ON a.id = t.id;
        """)
    
    # aggregation and sort
    c.execute("""
        SELECT a.country,
            SUM(a.beer_sevrings + a.spirit_servings + a.wine_servings) 
            AS total_alcohol_consumption
        FROM
            alcoholDB AS a
        GROUP BY
            a.country
        ORDER BY
            total_alcohol_consumption DESC;
    """)
    result = c.fetchone()
    conn.commit()
    conn.close()
    
    
    
    log_query("Complex Query")
    
    return result


if __name__ == "__main__":
    print(complex_query())