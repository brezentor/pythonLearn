import json
import sys

workfile = "D:\\python\\pythonLearn\\16. json.txt"

purgejson = open(workfile, mode = "w")
purgejson.close()

jsinf = open(workfile, mode = "a")

b = 1
d = 9
lsit = []
x = 0
while x < 10:
    b = b * 5
    d = d * 9
    dcit = {"a": b, "c": d}
    x += 1
    lsit.append(dcit)
try:
    json.dump(lsit, jsinf)
    jsinf.close()
except:
    print(sys.exc_info()[1])



jsop = open(workfile, mode = "r")
ls = json.load(jsop)
print(lsit[6])

