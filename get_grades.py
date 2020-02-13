# get_products.py
#challenge 2

print("REQUESTING SOME DATA FROM THE INTERNET...")

import requests
import json
import statistics


request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
print("URL: ", request_url)


response = requests.get(request_url)
print(type(response))
#print(dir(response)),  shows what you can do with the "response"

print(response.status_code)
print(type(response.text))

parsed_response = json.loads(response.text)
print(type(parsed_response)) #list variable

#for d in parsed_response:
 #   print(d["id"], d["name"])

#parsed_response.keys() or .values() or .items()
grades = [s["finalGrade"] for s in parsed_response["students"]]
print(grades)

average = statistics.mean(grades)
print(average)
