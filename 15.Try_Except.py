from urllib import request
import sys

writeerr = open(file = "D:\\python\\pythonLearn\\15.Try_Except.txt", mode = "a")
ipaddrs = "10.30.0.120"
myurl = "http://{ip}/admin/spacfg.xml"
mu = myurl.format(ip=ipaddrs)
try:
    answer = request.urlopen(mu)
except:
    print(sys.exc_info()[1])
    writeerr.write(ipaddrs+"\n")
    writeerr.close()
else:
    ans = answer.readlines()
    a = ans[13]
    mac = str(a).lstrip("""b'<MAC_Address group="Info/Product_Information\"""").lstrip(">").rstrip("n'").rstrip(
        "/MAC_Address>\\").rstrip("<")
    print(a)
    print(mac)