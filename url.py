from urllib import request

myurl = "http://10.30.0.77/admin/spacfg.xml"
answer = request.urlopen(myurl)
ans = answer.readlines()
a = ans[13]
mac = str(a).lstrip("""b'<MAC_Address group="Info/Product_Information">""").rstrip("n'").rstrip("</MAC_Address>\\")
print(mac)