import requests
def get():

    x = requests.get("https://www.google.com", verify="cacert.pem")
    display(x.status_code)


