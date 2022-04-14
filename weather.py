import requests

api_key = "2499e65f4a958ff5b07f90449e9efaeb"
city = "Orlando"
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+""

request = requests.get(url)
json = request.json()
print(json)

description = json.get("weather")[0].get("description")
print("Today's forecast is", description)
temp_min = json.get("main").get("temp_min")
print("The minimum temperature is", temp_min)
