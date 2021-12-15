# pip install pyodbc
# need to install mysql-connector-odbc-5.2.2 for mysql ver 14.14 distrib. 5.1.41
import pyodbc

connect = pyodbc.connect('DRIVER={MySQL ODBC 5.2w Driver}; SERVER=10.0.0.9; PORT=3306; DATABASE=dyndns; UID=root; PWD=Prolog1;')
cursor = connect.cursor()
query = ("""SELECT * FROM filials;""")
cursor.execute(query)
result = cursor.fetchall()
print(result)
connect.close()
l = len(result)
inf = []
onf = []
d = {}
d.
for n in range(0, l):
    inf.append(result[n][0])
    onf.append(result[n][2])
print(inf)
print(onf)