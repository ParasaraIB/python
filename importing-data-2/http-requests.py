# === Performing http requests in python using urllib ===

# import packages
from urllib.request import urlopen, Request
# specify the url
url = 'http://www.datacamp.com/teach/documentation'
# this packages the request: request
request = Request(url)
# sends the requests and cathces the response: response
response = urlopen(request)
# print the datatype of response
print(type(response))
# close response
response.close()

# === Printing http request results in python using urllib ===

# import packages
from urllib.request import urlopen, Request
# specify the url
url = 'http://www.datacamp.com/teach/documentation'
# this packages the request
request = Request(url)
# sends the request and catches the response: response
response = urlopen(request)
# extract the response: html
html = response.read()
# print the html
print(html)
# close the response
response.close()

# === Performing http request in python using requests ===

# import package
import requests
# specify the url: url
url = 'http://www.datacamp.com/teach/documentation'
# packages the request, send the request, and catch the response: r
r = requests.get(url)
# extract the response: text
text = r.text
# print the html
print(text)
