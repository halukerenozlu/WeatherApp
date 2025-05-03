from tkinter import *
from PIL import Image, ImageTk
import requests
url = 'https://api.openweathermap.org/data/2.5/weather'
api_key = 'eb430b60d10ab2aec84af32c6fcba58f'
icon_url = 'https://openweathermap.org/img/wn/{}@2x.png'


def get_weather(city):
    params = {'q': city, 'appid': api_key, 'lang': 'tr'}
    data = requests.get(url, params=params).json()
    if data:
        city = data['name']
        country = data['sys']['country']
        temp = int(data['main']['temp']-273.15)
        icon = data['weather'][0]['icon']
        condition = data['weather'][0]['description']
        return city, country, temp, icon, condition
