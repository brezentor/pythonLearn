def domain_name(url):
    if (url.find("https://") != -1):
        url = url.replace("https://", "")

    if (url.find("http://") != -1):
        url = url.replace("http://", "")

    if (url.find("www.") != -1):
        url = url.replace("www.", "")
    dot = url.find(".")
    suf = []
    for i in range(len(url)):
        if (i >= dot):
            suf.append(url[i])
    suf = "".join(suf)
    url = url.replace(suf, "")
    return url


url = "http://google.com"
print(domain_name(url))

#best practice

#def domain_name(url):
#    return url.split("://")[-1].split(".")[-2]