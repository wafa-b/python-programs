import requests

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='

city = input("Please Enter The city: ")

url = api_address + city

data = requests.get(url).json()

weather = data['weather']

print(weather[0]['description'])

