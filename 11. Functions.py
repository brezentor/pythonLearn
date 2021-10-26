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


#functions with dictionaries through MODULE 12 Lesson
#1
import module12dicti

s = input("Name?")
n = input("Age?")
zapis1 = module12dicti.dictionary(s, n)
print(zapis1)

#2

import module12dicti2

na = input("name? ")
ti = input("time? ")
ord = input("order? ")
module12dicti2.dicti(na, ti, ord)
module12dicti2.funcinfunc()