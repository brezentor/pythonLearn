from urllib import request

#tip = "D:\\python\\trueresults.log"
#iptest = open(tip, mode="r")
#for p in iptest:
  #ipaddrs = str(p)

ipaddrs = "10.30.0.77"
myurl = "http://{ip}/admin/spacfg.xml"
mu = myurl.format(ip = ipaddrs)
answer = request.urlopen(mu)
ans = answer.readlines()
a = ans[13]
mac = str(a).lstrip("""b'<MAC_Address group="Info/Product_Information">""").rstrip("n'").rstrip("</MAC_Address>\\")
print(mac)