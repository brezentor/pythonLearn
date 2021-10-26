import os

reserved = "D:\\python\\reserved.log"
truetest = "D:\\python\\true.log"
falsetest = "D:\\python\\false.log"
input = open(reserved, mode="r")
outputt = open(truetest, mode="w")
outputf = open(falsetest, mode="w")
for line in input:
  print(line)
  hostname = line  # example
  response = os.system("ping -n 2 " + hostname)

  # and then check the response...
  if response == 0:
    outputt.write(line)
  else:
    outputf.write(line)
input.close()
outputt.close()
outputf.close()

readt = open(truetest, mode="r")
readf = open(falsetest, mode="r")

print(readt.readlines())







