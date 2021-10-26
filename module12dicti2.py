#----------Dictionary 2--------------
d = []


def dicti(name, time, *order):
    ordertab = {
        'name': name,
        'time': time,
        'order': order
    }
    d.append(ordertab)
    print(d)


def funcinfunc():
    q = ""
    while (q != "n"):
        q = input("Any orders? Y or N? ")
        q = q.lower()
        if (q == "y"):
            na = input("name? ")
            ti = input("time? ")
            ord = input("order? ")
            dicti(na, ti, ord)
        elif (q == "n"):
            print("OK\n" + "Here an ordertab:")
            t = d.__len__()
            for p in range(0, t, 1):
                print(d[p])