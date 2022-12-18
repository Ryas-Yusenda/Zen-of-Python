import sqlite3
import pandas as pd

conn = sqlite3.connect('database.db')
cur = conn.cursor()

cur.execute("""
            CREATE TABLE IF NOT EXISTS Persons (
                Personid INTEGER PRIMARY KEY AUTOINCREMENT,
                LastName varchar(255) NOT NULL,
                FirstName varchar(255) NOT NULL
                )
                """)

cur.execute("""
            INSERT INTO Persons (FirstName,LastName) VALUES
            ('Lars','Monsen');
            """)

conn.commit()

sql = pd.read_sql_query("SELECT * FROM Persons", conn)
df = pd.DataFrame(sql, columns=['Personid', 'LastName', 'FirstName'])

print(df)