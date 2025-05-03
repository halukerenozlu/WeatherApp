from tkinter import *
from PIL import Image, ImageTk
import requests
from havadurumu import get_weather, icon_url


def main():
    city = cityEntry.get()
    weather = get_weather(city)

    if weather:
        locationLabel['text'] = '{},{}'.format(weather[0], weather[1])
        templabel['text'] = '{}°C'.format(weather[2])
        conditionLabel['text'] = weather[4]
        icon = ImageTk.PhotoImage(Image.open(requests.get(
            icon_url.format(weather[3]), stream=True).raw))
        iconLabel.configure(image=icon)
        iconLabel.image = icon


app = Tk()
app.geometry('500x500')
app.title('Hava durumu')

cityEntry = Entry(app, justify=CENTER)
cityEntry.pack(fill=BOTH, ipady=10, padx=18, pady=5)
cityEntry.focus()

searchButton = Button(app, text='Arama', font=('Arial', 15), command=main)
searchButton.pack(fill=BOTH, ipady=10, padx=20)

iconLabel = Label(app)
iconLabel.pack()

locationLabel = Label(app, font=('Arial', 40))
locationLabel.pack()

templabel = Label(app, font=('Arial', 50, 'bold'))
templabel.pack()

conditionLabel = Label(app, font=('Arial', 20))
conditionLabel.pack()

app.mainloop()
