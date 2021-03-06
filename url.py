from urllib import request
import sys
import json
import re
import paramiko

host = "10.30.0.6"
port = 22
username = "iptel"
password = "48qtnRXt"

arpres = "D:\\python\\arp.log"
tip = "D:\\python\\trueresults.log"
arper = "D:\\python\\arp_error.log"
jsonfile = "D:\\python\\allinfo.log"

purjson = open(jsonfile, mode = "w")
purgarp = open(arpres, mode = "w")
purgarper = open(arper, mode = "w")
purgarp.close()
purgarper.close()
purjson.close()

writeerr = open(arper, mode = "a")
iptest = open(tip, mode="r")
sizetest = open(tip, mode="r")
arpresults = open(arpres, mode = "a")
allfile = open(jsonfile, mode = "a")

count = 1
info = sizetest.readlines()
size = len(info)
sizetest.close()

alfi = []

for p in iptest:
    countres = "{co} of {si}"
    countresult = countres.format(co = str(count), si = str(size))
    endres = "{en} of {en}"
    endresult = endres.format(en = str(size))
    if countresult == endresult:
        print("End")
    else:
        print(countresult)
    count += 1
    ipaddrs = str(p).rstrip(' \n')
    myurl = "http://{ip}/admin/spacfg.xml"
    mu = myurl.format(ip=ipaddrs)
    try:
        answer = request.urlopen(mu)
    except:
        print(sys.exc_info()[1])
        writeerr.write(ipaddrs + "\n")
    else:
        ans = answer.readlines()
        findnumber = r"<User_ID_1_ group=\"Ext_1/Subscriber_Information\">[0-9]{3}</User_ID_1_>"
        results1 = re.findall(findnumber, str(ans))
        findre = r"[0-9]{3}"
        number = re.findall(findre, str(results1))

        findmac = r"<MAC_Address group=\"Info/Product_Information\">[0-9, A-Z]{12}</MAC_Address>"
        results2 = re.findall(findmac, str(ans))
        findres = r"[0-9, A-Z]{12}"
        macad = re.findall(findres, str(results2))

        findmod = r"<Product_Name group=\"Info/Product_Information\">[0-9, A-Z, -]{7}</Product_Name>"
        results3 = re.findall(findmod, str(ans))
        findresult = r"[0-9, A-Z, -]{7}"
        model = re.findall(findresult, str(results3))

        command_koza = """mysql -u asterisk -pyw7s72ad1d2esd3qd3 asterisk -e 'select name from users where extension="{mun}"'"""
        command = command_koza.format(mun=number[0])
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)
        stdin, stdout, stderr = ssh.exec_command(command)
        dataraw = stdout.read() + stderr.read()
        loc = str(dataraw).lstrip("b'name\\n").rstrip("n'").rstrip("\\")
        print(loc)
        ssh.close()

        loginfo = "{macf} - {ipf} - {modf} - {numf} - {locat}\n"
        arpresults.write(loginfo.format(macf = macad[0], ipf = ipaddrs, modf = model[0], numf = number[0], locat = loc))

        info = {"MacAddress" : macad[0], "IpAddress" : ipaddrs, "PhoneModel": model[0], "Number": number[0], "Location": loc}
        alfi.append(info)


try:
    myjson = json.dump(alfi, allfile)
except:
    print(sys.exc_info()[1])

writeerr.close()
iptest.close()
arpresults.close()
allfile.close()