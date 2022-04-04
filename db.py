# import sqlite3

# conn = sqlite3.connect('stock.db')
import psycopg2

# print(conn)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS kospi")
cur.execute("""
            CREATE TABLE kospi(
                "Id" INTEGER PRIMARY KEY,
                "Symbol" VARCHAR(12),
                "Market" VARCHAR(10),
                "Name" VARCHAR(128),
                "Sector" VARCHAR(256),
                "Industry" VARCHAR(256),
                "ListingDate" VARCHAR(256),
                "SettleMonth" VARCHAR(12),
                "Representative" VARCHAR(256),
                "HomePage" VARCHAR(256),
                "Region" VARCHAR(256));
            """)
# conn.commit()
# conn.close()

import FinanceDataReader as fdr
import pandas as pd

stocks = fdr.StockListing('KOSPI') # 코스피
stocks.fillna("null",inplace = True)
stocks = stocks.astype('string')

id_ = 1
for i in range(len(stocks)):
    cur.execute("""INSERT INTO kospi("Id", "Symbol", "Market", "Name", "Sector", "Industry", "ListingDate","SettleMonth", "Representative", "HomePage", "Region") VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
    """, (id_, stocks.iloc[i][0],stocks.iloc[i][1],stocks.iloc[i][2],stocks.iloc[i][3],stocks.iloc[i][4],stocks.iloc[i][5],stocks.iloc[i][6],stocks.iloc[i][7],stocks.iloc[i][8],stocks.iloc[i][9]))
    id_ += 1
conn.commit()
conn.close()

# PostgreSQL Index usage  Should be 99% for every table with more than 10 000 rows
# postgresql 인덱스 초과