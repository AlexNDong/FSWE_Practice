import requests

# The "requests" library has been installed since the install of FastAPI
# We can use it to test API route instead of going to Web-browser to test it using HTTP URL
print(requests.get("http://0.0.0.0:8000/substract/10/5").json())
print(requests.get("http://0.0.0.0:8000/devide/100?b=10").json())