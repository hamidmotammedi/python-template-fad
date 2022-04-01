import requests
# get Request to https://www.metaweater.com/api/location/search/?query=bremen
params = {'query': 'bremen'}
header = {'Content-Type': 'application/json'}
result = requests.get('https://www.metaweather.com/api/location/search/',
                      params=params,
                      headers=headers,)
json = result.json()
print(result)  # <Response [200]>
print('json Response:', json)  # 200
print('City name:', json[0]['title'])
