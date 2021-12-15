# pip install pyodbc
import pyodbc

connect = pyodbc.connect('DRIVER={SQL Server}; SERVER=10.0.0.9; PORT=1433; DATABASE=IpTele; UID=sa; PWD=123456;')
cursor = connect.cursor()
query = ("""SELECT * FROM [dbo].[IpTelephony]""")
cursor.execute(query)
result = cursor.fetchall()
print(result[0])
connect.close()