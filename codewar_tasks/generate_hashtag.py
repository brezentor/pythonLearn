def generate_hashtag(s):
    r = ["#"]
    h = ""
    for i in s:
        if ((i.isalpha() == True) or (i.isspace() == True)):
            r.append(i)
            h = "".join(r)
    h = h.title().replace(" ", "")
    if ((len(h) >= 140) or (h == "")):
        return False
    return h


s = "SHOULD CAPIT?ALIZE 3FIRST 23 LETTERS OF 1WORDS!"
print(generate_hashtag(s))