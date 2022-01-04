def valid_parentheses(string):
    res = []
    if (string.count("(") != string.count(")")):
        return False
    for i in string:
        if ((i == "(") or (i == ")")):
            res.append(i)
    r = "".join(res)
    for j in range (r.count("(")):
        r = r.replace("()", "")
    if (r == ""):
        return True
    else:
        return False

string = "hi()()"
print(valid_parentheses(string))