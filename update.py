from PIL import Image, ImageTk
import requests
from havadurumu import icon_url

def guncelle(weather, locationLabel, templabel, conditionLabel, iconLabel):
    if weather:
        locationLabel['text'] = '{},{}'.format(weather[0], weather[1])
        templabel['text'] = '{}°C'.format(weather[2])
        conditionLabel['text'] = weather[4]
        icon = ImageTk.PhotoImage(Image.open(requests.get(
            icon_url.format(weather[3]), stream=True).raw))
        iconLabel.configure(image=icon)
        iconLabel.image = icon
