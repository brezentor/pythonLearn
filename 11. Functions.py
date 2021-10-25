# functions with fuctorial


def fuct(n):
    """variant 1 Calculate fuctorial of n"""
    num = []
    m = 1
    n = int(n)
    for n in range (0, n, 1):
        num.append(n+1)
        m = num.pop() * m
    print("fuctorial is", m)


n = input("you want to know factorial of - ")
n = str(n)
fuct(n)


def fuctorial(x):
    """variant 2 Calculate fuctorial of x"""
    answer = 1
    for i in range (1, x + 1):
        answer = answer * i
    return answer

print(fuctorial(5))


#functions with dictionaries
#1

def dictionary(string, integrior):
    zapis = {
        'letter': string,
        'number': integrior
    }
    return zapis

s = input("Name?")
n = input("Age?")
zapis1 = dictionary(s, n)
print(zapis1)

#2

d = []
na = ""
ti = ""
ord = ""

def dicti(name, time, *order):
    ordertab = {
        'name': name,
        'time': time,
        'order': order
    }
    d.append(ordertab)
    print(d)

na = input("name? ")
ti = input("time? ")
ord = input("order? ")
dicti(na, ti, ord)
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
        for p in range (0, t, 1):
            print(d[p])