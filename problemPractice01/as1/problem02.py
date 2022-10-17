""" Here i use open api weather api  """
import json
import time
import requests

lat = "23.85"
lon = "90.26"
api_key = "0a0e8b3578f69ef0b83d7415faf94d28"
weather_api = "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid="+api_key


def weather_data():
    # get data from api
    response = requests.get(weather_api)
    data = response.content.decode('UTF-8')
    # convert string to json and get temperature
    dict_data = json.loads(data)
    weather_dict = dict_data['main']
    temp = weather_dict['temp']  # get temperature in kelvin scale
    temp_in_celsius = (temp-273.15)
    # print temperature
    print(temp_in_celsius) 
    while True:
        # update every after 30 min
        time.sleep(1800)
        weather_data() 


weather_data()


