import requests

api_address = 'http://api.openweathermap.org/data/2.5/weather?q=Nongstoin&appid=78b2696f2a6015b511d94ac703293df8'
json_data = requests.get(api_address).json()

def temp():
    temperature = round(json_data['main']['temp']-273,1)
    return temperature

def des():
    description = json_data["weather"][0]["description"]
    return description

#print(temp())
#print(des())