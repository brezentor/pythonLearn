def create_phone_number(n):
    a = b = c = ""
    for i in n[0:3]:
        a = str(a) + str(i)
    for i in n[3:6]:
        b = str(b) + str(i)
    for i in n[6:]:
        c = str(c) + str(i)
    res = "({q}) {w}-{e}".format(q = a, w = b, e = c)
    print(res)

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
create_phone_number(n)

# best practice

def create_phone_number(b):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*b)

b = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(create_phone_number(b))