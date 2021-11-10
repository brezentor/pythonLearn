# pip install pyodbc
import pyodbc
import json
import sys

datapath = "D:\\python\\allinfo.log"
readdata = open(datapath, mode = "r")

data = json.load(readdata)

inf = len(data)
messagestart = "Starting to insert {suminf} element(s) to SQL table...".format(suminf = inf)
print(messagestart)

counter = 0
countermes = 1

for n in data:
    mac = data[counter]['MacAddress']
    ip = data[counter]['IpAddress']
    model = data[counter]['PhoneModel']
    num = data[counter]['Number']
    loc = "HO"
    invnum = "unknown{c}".format(c = counter) # until dont made a script to get a invnumber
    messageproc = "{l} of {k}".format(l = countermes, k = inf)
    print(messageproc)
    counter += 1
    countermes += 1

    try:
        conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=10.0.0.9; PORT=1433; DATABASE=IpTele; UID=sa; PWD=123456;')
    except:
        print(sys.exc_info()[1])
    else:
        cursor = conn.cursor()
        query = ("""
                        INSERT INTO [dbo].[IpTelephony] ([MacAddress], [IpAddress], [PhoneName], [InvNumber], [PhoneNumber], [Location])
                        VALUES ('{m}', '{i}', '{mod}', '{inv}', '{n}', '{l}')
                        """).format(m=str(mac), i=str(ip), mod=str(model), inv=str(invnum), n=str(num), l=str(loc))
        try:
            cursor.execute(query)
        except:
            print(sys.exc_info()[1])
        else:
            conn.commit()
            conn.close()

print("Inserting to SQL table is complete")