# pip install pyodbc
import pyodbc



conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=10.0.0.9; PORT=1433; DATABASE=IpTele; UID=sa; PWD=123456;')
cursor = conn.cursor()
query = ("""
            INSERT INTO [dbo].[IpTelephony] ([MacAddress], [IpAddress], [PhoneName], [InvNumber], [PhoneNumber], [Location]) 
            VALUES ('{m}', '{i}', '{mod}', '{inv}', '{n}', '{l}')
            """)
print(query)
cursor.execute(query)
conn.commit()
conn.close()