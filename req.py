import urllib.request
import ssl

def get():
    url = "https://www.google.com"
    context = ssl.create_default_context()
    handler = urllib.request.HTTPSHandler(context=context)
    opener = urllib.request.build_opener(handler)
    response = opener.open(url)
    print(response.code)
get()