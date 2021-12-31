def dirReduc(arr):
    res = []
    n = arr.count("NORTH")
    s = arr.count("SOUTH")
    w = arr.count("WEST")
    e = arr.count("EAST")
    print("north = " + str(n) + " south = " + str(s) + " west = " + str(w) + " east = " + str(e))
    if ((n == 1) and (s == 1) and (w == 1) and (e == 1)):
        res = arr
    else:
        if (n == s):
            pass
        elif (n != s):
            if (n > s):
                res.append("NORTH")
            elif (n < s):
                res.append("SOUTH")

        if (w == e):
            pass
        elif (w != e):
            if (w > e):
                res.append("WEST")
            elif (w < e):
                res.append("EAST")
    print(arr)
    return res



arr = ["NORTH", "WEST", "SOUTH", "SOUTH", "EAST"]
print(dirReduc(arr))