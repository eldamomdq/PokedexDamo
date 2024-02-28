import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter
import urllib3
from io import BytesIO

window = tkinter.Tk()
window.geometry ("600x500")
window.title("La Pokedex de Damo")
window.config (padx=10, pady=10)

title_label = tkinter.Label(window, text="Damodex")
title_label.config(font=("Arial", 32))
title_label.pack(padx=10, pady=10)

pokemon_image =tkinter.Label(window)
pokemon_image.pack()

pokemon_information =tkinter.Label(window)
pokemon_information.config(font=("Arial", 20))
pokemon_information.pack(padx=10, pady=10)

pokemon_types =tkinter.Label(window)
pokemon_types.config(font=("Arial", 20))
pokemon_types.pack(padx=10, pady=10)

def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}")
    pokemon_types.config(text=f"{pokemon.types}")




label_id_name = tkinter.Label(window, text="ID or Name")
label_id_name.config(font=("Arial", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tkinter.Text(window, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

btn_load = tkinter.Button (window, text="Load Pokemon", command=load_pokemon)
btn_load.config(font=("Arial", 20))
btn_load.pack (padx=10, pady=10)

window.mainloop()
