import requests
def get():

    x = requests.get("https://www.google.com", verify=False)
    display(x.status_code)


