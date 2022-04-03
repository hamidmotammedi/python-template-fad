import requests
import json

location_search = 'location/search/'
location = 'location/'

# Aufgabe 1.1
base_url = 'https://www.metaweather.com/api/'

params = {'query': 'Bremen'}

response = requests.get(base_url + location_search, params)

json = response.json()

print('response code:', response.status_code)
print('response json:', json)
print('response json:', json[0]['woeid'])

# Aufgabe 1.2

woeid = json[0]['woeid']

response_weather_bremen = requests.get(base_url + location + str(woeid))

# print('response_weather_bremen code:', response_weather_bremen.status_code)
# print('response_weather_bremen json:', response_weather_bremen.json())


# print(json.dumps(response_weather_bremen.json()))

# Aufgabe 1.3

response_weather_bremen_march = requests.get(
    base_url + location + str(woeid) + '/2019/3/8/')
print('resonse_weather_berin_march: ', response_weather_bremen.json())
