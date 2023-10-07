"""
Transforms and Loads data into the local SQLite3 database
"""
import os
from databricks import sql
import pandas as pd
from dotenv import load_dotenv

#load the csv file and insert into a new sqlite3 database
def load(dataset="data/alcohol.csv", dataset1="data/toy.csv"):
    df = pd.read_csv(dataset, delimiter=",", skiprows=1)
    df2 = pd.read_csv(dataset1)
    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    # print(server_h)
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        c.execute("DROP TABLE IF EXISTS alcoholDB")
        c.execute("SHOW TABLES FROM default LIKE 'alcohol*'")
        result = None
        if not result:
            c.execute(
                """
                CREATE TABLE alcoholDB (
                    country string, 
                    beer_servings int,
                    spirit_servings int,
                    wine_servings int,
                    total_pure_alcohol real,
                    id int
                )
                """
            )
            for row in df.iterrows():
                convert = tuple(row)
                print(convert)
                c.execute(f"INSERT INTO alcoholDB VALUES {convert}")
        c.execute("SHOW TABLES FROM default LIKE 'toy*'")
        # result = c.fetchall()
        c.execute("DROP TABLE IF EXISTS toyDB")
        result = None
        if not result:
            c.execute(
                    """
                    CREATE TABLE IF NOT EXISTS ToyDB (
                        id int,
                        value int
                    )
                    """
            )
            for _, row in df2.iterrows():
                convert = tuple(row)
                c.execute(f"INSERT INTO toyDB VALUES {convert}")
        c.close()

    return "success"
