def validBraces(string):
    a = []
    for i in string:
        if ((i == "{") or (i == "}") or (i == "[") or(i == "]") or (i == "(") or (i == ")")):
            a.append(i)
    a = "".join(a)
    if ((a.count("(") != a.count(")")) or (a.count("{") != a.count("}")) or (a.count("[") != a.count("]"))):
        return False
    w = " "
    b = 0
    c = len(a)
    while (c != b):
        a = a.replace("[]", "").replace("{}", "").replace("()", "")
        c = c - 1
    if (a != ""):
        return False
    else:
        return True

string = "[{()}]"
print(validBraces(string))

# best practice:

#def validBraces(s):
#  while '{}' in s or '()' in s or '[]' in s:
#      s=s.replace('{}','')
#      s=s.replace('[]','')
#      s=s.replace('()','')
#  return s==''