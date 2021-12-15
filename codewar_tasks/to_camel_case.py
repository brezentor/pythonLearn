"""Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"""

def to_camel_case(text):
    if (text != ""):
        if (text[0].istitle()):
            if ((text.find("-") != -1) and (text.find("_") != -1)):
                result = 1
                q = text.split("-")
                for i in range(0, len(q)):
                    p = q.pop(i)
                    q.insert(i, p.title())
                res = "".join(q)
                q = res.split("_")
                result = "".join(q)

            elif (text.find("-") != -1):
                q = text.split("-")
                for i in range(0, len(q)):
                    p = q.pop(i)
                    q.insert(i, p.title())
                result = "".join(q)

            elif (text.find("_") != -1):
                q = text.split("_")
                for i in range(0, len(q)):
                    p = q.pop(i)
                    q.insert(i, p.title())
                result = "".join(q)

        elif (text[0].islower()):
            if ((text.find("-") != -1) and (text.find("_") != -1)):
                result = 1
                q = text.split("-")
                for i in range(1, len(q)):
                    p = q.pop(i)
                    q.insert(i, p.title())
                res = "".join(q)
                q = res.split("_")
                result = "".join(q)
            elif (text.find("-") != -1):
                q = text.split("-")
                for i in range(1, len(q)):
                    p = q.pop(i)
                    q.insert(i, p.title())
                result = "".join(q)

            elif (text.find("_") != -1):
                q = text.split("_")
                for i in range(1, len(q)):
                    p = q.pop(i)
                    q.insert(i, p.title())
                result = "".join(q)

    else:
        result = 'error'
    return result

inp = input("input\n")
print(to_camel_case(inp))

"""BEST PRACTICE"""
"""def to_camel_case(text):
    return text[0] + ''.join([w[0].upper() + w[1:] for w in text.replace("_", "-").split("-")])[1:] if text else ''
f = input("input\n")
print(to_camel_case(f))"""