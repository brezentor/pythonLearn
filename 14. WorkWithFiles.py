fileread = "D:\\python\\pythonLearn\\1. variables (змінні).py"
filewrite = "D:\\python\\pythonLearn\\14. WorkWithFiles.txt"
readf = open(fileread, mode = "r")
re = readf.readlines()
readf.close()
print(re)
writef = open(filewrite, mode = "a")
writef.write(re[0])
writef.close()
