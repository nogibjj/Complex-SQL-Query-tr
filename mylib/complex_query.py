"""
Design a complex SQL query 
involving joins, aggregation, and sorting
"""

import sqlite3
from mylib.query import log_query

LOG_FILE = "query_log.md"


def complex_query():
    """joins, aggregation, sorting"""
    conn = sqlite3.connect("alcoholDB.db")
    c = conn.cursor()
    c.execute()
    
    conn.commit()
    conn.close()
    
    log_query(f"")