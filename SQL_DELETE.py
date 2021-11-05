# pip install pyodbc
import pyodbc

ip = "10.30.0.196"
conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=10.0.0.9; PORT=1433; DATABASE=IpTele; UID=sa; PWD=123456;')
cursor = conn.cursor()
query = ("""
            DELETE FROM [dbo].[IpTelephony]
            WHERE [IpAddress] = '{i}'
            """).format(i = str(ip))
print(query)
cursor.execute(query)
conn.commit()
conn.close()