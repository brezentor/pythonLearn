from urllib import request
import sys
import json

""""""
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
arpresults = open(arpres, mode = "a")
allfile = open(jsonfile, mode = "a")

counter = 0
alfi = []

for p in iptest:
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
        a = ans[13]
        mac = str(a).lstrip("""b'<MAC_Address group="Info/Product_Information\"""").lstrip(">").rstrip("n'").rstrip(
        "/MAC_Address>\\").rstrip("<")
        model = ans[9]
        tel = str(model).lstrip("""b'<Product_Name group="Info/Product_Information\"""").lstrip(">").rstrip("n'").rstrip(
        "/Product_Name>\\").rstrip("<")
        print(a)
        arpresults.write(mac + " - " + ipaddrs + " - " + tel + "\n")

        info = {"MacAddress" : mac, "IpAddress" : ipaddrs, "PhoneModel": tel, "ID": counter}
        alfi.append(info)
        counter += 1

try:
    myjson = json.dump(alfi, allfile)
except:
    print(sys.exc_info()[1])

writeerr.close()
iptest.close()
arpresults.close()
allfile.close()