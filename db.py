import sqlite3

conn = sqlite3.connect('stock.db')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS kospi")
cur.execute("""
            CREATE TABLE kospi(
                "Id" INTEGER,
                "Symbol" VARCHAR(12),
                "Market" VARCHAR(10),
                "Name" VARCHAR(128),
                "Sector" VARCHAR(256),
                "Industry" VARCHAR(256),
                "ListingDate" DATETIME,
                "SettleMonth" VARCHAR(12),
                "Representative" VARCHAR(256),
                "HomePage" VARCHAR(256),
                "Region" VARCHAR(256));
            """)

conn.commit()
conn.close()