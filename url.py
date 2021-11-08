from urllib import request
import sys

arpres = "D:\\python\\arp.log"
tip = "D:\\python\\trueresults.log"
arper = "D:\\python\\arp_error.log"

purgarp = open(arpres, mode = "w")
purgarper = open(arper, mode = "w")
purgarp.close()
purgarper.close()

writeerr = open(arper, mode = "a")
iptest = open(tip, mode="r")
arpresults = open(arpres, mode = "a")

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
        print(a)
        arpresults.write(mac + " - " + ipaddrs + "\n")

writeerr.close()
iptest.close()
arpresults.close()