def tower_builder(n):
    asterisk = ["*"]
    res = []
    step = [1]
    for i in range (n-1):
        asterisk.append("*")
        asterisk.append("*")
    for j in range (1, n*2, 2):
        step.append(j+2)
        if (j == 0):
            res.append("*")
        else:
            res.append("".join(asterisk[:j]))
    s = res[-1].count("*")
    for e in reversed(res):
        e_c = e.count("*")
        if (e_c != s):
            spcs = (int(s) - int(e_c)) // 2
            new_e = e
            for num in range (0, spcs):
                new_e = " " + new_e + " "
            idn = res.index(e)
            res.remove(e)
            res.insert(idn, new_e)
        else:
            pass
    return res

n = 4
print(tower_builder(n))

#BEST PRACTICE

#def tower_builder(n):
#    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]