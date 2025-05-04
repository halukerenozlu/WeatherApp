from tkinter import *
from havadurumu import get_weather
from update import guncelle
from page import panel


def main():
    city = cityEntry.get()
    weather = get_weather(city)
    guncelle(weather, locationLabel, templabel, conditionLabel, iconLabel)


app = Tk()
app.geometry('500x500')
app.title('Hava durumu')

# Paneli kur, widget'ları al
cityEntry, locationLabel, templabel, conditionLabel, iconLabel = panel(app, main)


app.mainloop()




