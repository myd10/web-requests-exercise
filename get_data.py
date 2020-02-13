# get_data.py
#challenge 1

print("REQUESTING SOME DATA FROM THE INTERNET...")

import requests
import json


request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/1.json"
print("URL: ", request_url)


response = requests.get(request_url)
print(type(response))
#print(dir(response)),  shows what you can do with the "response"



print(response.status_code)
print(response.text)


parsed_response = json.loads(response.text)
print(type(parsed_response))
print(parsed_response["name"])


#breakpoint()


