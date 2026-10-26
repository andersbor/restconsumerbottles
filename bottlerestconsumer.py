import requests 
# install this library from the command line: 
# python -m pip install requests

BASE_URL = "http://localhost:5171/api/bottles"
# REST API with no JWT authentication, for now

response = requests.get(BASE_URL, verify=False)
# verify=False is used to ignore SSL certificate verification errors
# run with python -W ignore bottlerestconsumer.py to ignore the warning about SSL certificate verification
print(f"GET status code {response.status_code}")
if response.status_code == 200:
  print(response.json())

BOTTLE_DICTIONARY = {
    "volume": 45,
    "name": "Harboe citrus"
}

response = requests.post(BASE_URL, json=BOTTLE_DICTIONARY, verify=False)
# json= automatically converts the dictionary to a JSON string
# json= automatically sets the Content-Type header to application/json
 
print(f"POST status code {response.status_code}")
if response.status_code == 201:
  print(response.json())  

url = BASE_URL + "/1"
response = requests.delete(url, verify=False)
print(f"DELETE status code {response.status_code}")
if response.status_code == 200:
    print(response.json())

url = f"{BASE_URL}/2"
response= requests.put(url, json=BOTTLE_DICTIONARY, verify=False)
print(f"PUT status code {response.status_code}")
if response.status_code == 200:
  print(response.json())