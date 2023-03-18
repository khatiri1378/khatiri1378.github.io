import urllib.request

def get():
    url = "https://www.google.com"
    response = urllib.request.urlopen(url)
    print(response.code)
get()