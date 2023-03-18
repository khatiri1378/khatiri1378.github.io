import requests
def get():

    x = requests.get("https://www.google.com")
    display(x.status_code)


