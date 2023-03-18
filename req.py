import urllib.request
import ssl

def get():
    url = "https://www.google.com"
    context = ssl.create_default_context()
    context.set_ciphers('DEFAULT:@SECLEVEL=1')
    context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
    handler = urllib.request.HTTPSHandler(context=context)
    opener = urllib.request.build_opener(handler)
    response = opener.open(url)
    print(response.code)
get()