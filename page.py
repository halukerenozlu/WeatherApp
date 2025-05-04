from tkinter import *

def panel(app, main_command):
    cityEntry = Entry(app, justify=CENTER)
    cityEntry.pack(fill=BOTH, ipady=10, padx=18, pady=5)
    cityEntry.focus()

    searchButton = Button(app, text='Arama', font=('Arial', 15), command=main_command)
    searchButton.pack(fill=BOTH, ipady=10, padx=20)

    iconLabel = Label(app)
    iconLabel.pack()

    locationLabel = Label(app, font=('Arial', 40))
    locationLabel.pack()

    templabel = Label(app, font=('Arial', 50, 'bold'))
    templabel.pack()

    conditionLabel = Label(app, font=('Arial', 20))
    conditionLabel.pack()

    # Gerekli widget'ları döndürüyoruz
    return cityEntry, locationLabel, templabel, conditionLabel, iconLabel
