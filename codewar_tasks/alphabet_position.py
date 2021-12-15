def alphabet_position(text):
    d = {'a': '1', 'b':'2', 'c':'3', 'd':'4', 'e':'5', 'f':'6', 'g':'7', 'h':'8', 'i':'9', 'j':'10', 'k':'11', 'l':'12',
         'm':'13', 'n':'14', 'o':'15', 'p':'16', 'q':'17', 'r':'18', 's':'19', 't':'20', 'u':'21', 'v':'22', 'w':'23',
         'x':'24', 'y':'25', 'z':'26'}
    b = text.lower()
    l = len(b)
    res = ""
    for m in range(0, l):
        if (b[m].isalpha() != True):
            pass
        else:
            res = res + "{" + b[m] + "} "
    result = res.format_map(d).rstrip(" ")
    print(result)


text = "The sunset sets at twelve o' clock."
alphabet_position(text)

# best practice

def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

text = "Compare with your solution!"
print(alphabet_position(text))