def domain_name(url):
    return url.split("://")[-1].split(".")[-2]

url = "http://google.com"
print(domain_name(url))