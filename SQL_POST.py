# pip install pyodbc
import pyodbc


mac = "e05fb9821627"
ip = "10.30.0.196"
model = "Cisco SPA502g"
invnum = "TELE50"
num = "523"
loc = "RD"
conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=10.0.0.9; PORT=1433; DATABASE=IpTele; UID=sa; PWD=123456;')
cursor = conn.cursor()
query = ("""
            INSERT INTO [dbo].[IpTelephony] ([MacAddress], [IpAddress], [PhoneName], [InvNumber], [PhoneNumber], [Location]) 
            VALUES ('{m}', '{i}', '{mod}', '{inv}', '{n}', '{l}')
            """).format(m = str(mac), i = str(ip), mod = str(model), inv = str(invnum), n = str(num), l = str(loc))
print(query)
cursor.execute(query)
conn.commit()
conn.close()