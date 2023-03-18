import requests
import urllib3

def get():

    x = requests.get("https://www.google.com")
    urllib3.disable_warnings()
    display(x.status_code)


