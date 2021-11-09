import re
from urllib import request
import sys

ipaddrs = "10.30.0.150"
myurl = "http://{ip}/admin/spacfg.xml"
mu = myurl.format(ip=ipaddrs)
try:
    answer = request.urlopen(mu)
except:
    print(sys.exc_info()[1])
else:
    ans = answer.read()
    findnumber = r"<User_ID_1_ group=\"Ext_1/Subscriber_Information\">[0-9]{3}</User_ID_1_>"
    results1 = re.findall(findnumber, str(ans))
    print(results1)
    findre = r"[0-9]{3}"
    number = re.findall(findre, str(results1))
    print(number[0])

    findmac = r"<MAC_Address group=\"Info/Product_Information\">[0-9, A-Z]{12}</MAC_Address>"
    results2 = re.findall(findmac, str(ans))
    print(results2)
    findres = r"[0-9, A-Z]{12}"
    macad = re.findall(findres, str(results2))
    print(macad[0])

    findmod = r"<Product_Name group=\"Info/Product_Information\">[0-9, A-Z, -]{7}</Product_Name>"
    results3 = re.findall(findmod, str(ans))
    print(results3)
    findresult = r"[0-9, A-Z, -]{7}"
    model = re.findall(findresult, str(results3))
    print(model[0])