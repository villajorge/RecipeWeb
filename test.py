# import requests
import http.client
import json
import pprint

# url = "edamam-food-and-grocery-database.p.rapidapi.com"
# conn = http.client.HTTPSConnection(url)

# ingredient = "eggs"

# # querystring = {"ingr":ingredient}

# headers = {
# 	"X-RapidAPI-Key": "a174ac89eamshf7c57f29f424319p17a06djsn41bb1dfbf0f3",
# 	"X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
# }

# conn.request("GET",f"/api/food-database/v2/parser?ingr={ingredient}", headers=headers)
# # response = requests.get(url, headers=headers, params=querystring)
# res =conn.getresponse()
# data = res.read()
# # print(response.json)

# string = data.decode("utf-8")
# diction = json.loads(string)

# pprint.pprint(diction["hints"][0]["food"]["uri"])

#print(diction)

# ingr = "chicken"
    
# url = "themealdb.p.rapidapi.com"
# conn = http.client.HTTPSConnection(url)
# headers = {
# 	        'X-RapidAPI-Key': "a174ac89eamshf7c57f29f424319p17a06djsn41bb1dfbf0f3",
#             'X-RapidAPI-Host': "themealdb.p.rapidapi.com"
#         }
# conn.request("GET",f"/filter.php?i={ingr}", headers=headers)
# res =conn.getresponse()
# data = res.read()
# diction = json.loads(data)
# print(diction)

diction = {
    "test1": "apple",
    "test2": "pear",
    "amount1": "whole",
    "amount2": "half"
}

for i in range(1,3):
    print(diction["amount"+str(i)], diction["test"+str(i)])