import pycurl

# Create a new curl object
curl = pycurl.Curl()

# Set the URL to make the request to
curl.setopt(pycurl.URL, "http://www.google.com")

# Set any additional options you need, such as headers or data to send in the request
curl.setopt(pycurl.HTTPHEADER, ["Content-Type: application/json"])

# Set a callback function to handle the response
response = []
def handle_response(data):
    response.append(data)

curl.setopt(pycurl.WRITEFUNCTION, handle_response)

# Perform the request
curl.perform()

# Check the response code and any response data
http_code = curl.getinfo(pycurl.RESPONSE_CODE)
print(f"Response code: {http_code}")


# Clean up
curl.close()
