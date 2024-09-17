import tkinter as tk
import random
from tkinter import *

tomaatinheitinIkkuna = tk.Tk()

tomaatinheitinIkkuna.title("Tomaatinheitin")
tomaatinheitinIkkuna.geometry('1920x1080')

# Configuration for grid layout
tomaatinheitinIkkuna.grid_rowconfigure(0, weight=0)
tomaatinheitinIkkuna.grid_columnconfigure(0, weight=1)

tomaatinheitinIkkuna.grid_rowconfigure(1, weight=1)
tomaatinheitinIkkuna.grid_columnconfigure(1, weight=1)

tomaatinheitinIkkuna.grid_rowconfigure(2, weight=0)
tomaatinheitinIkkuna.grid_columnconfigure(2, weight=1)

# Kernestis Image
imageKernesti = PhotoImage(file="kerne.png")
imageLabelKernesti = tk.Label(tomaatinheitinIkkuna, image=imageKernesti)
imageLabelKernesti.grid(row=random.randint(0, 2), column=0, sticky="w")

# Maalitaulu Image
imageMaalitaulu = PhotoImage(file="maalitaulu.png")
imageLabelMaalitaulu = tk.Label(tomaatinheitinIkkuna, image=imageMaalitaulu)
imageLabelMaalitaulu.grid(row=1, column=1)

onkoPainettu = False

# Ernestis Image
def image_ernesti():
    imageErnesti = PhotoImage(file="erne.png")
    imageLabelErnesti = tk.Label(tomaatinheitinIkkuna, image=imageErnesti)
    imageLabelErnesti.image = imageErnesti 
    imageLabelErnesti.grid(row=random.randint(0, 2), column=2, sticky="e")

def show_ernesti():
    print("Hei")
    global onkoPainettu
    if onkoPainettu == False:
        image_ernesti()
        print(onkoPainettu)
        onkoPainettu = True
        print(onkoPainettu)
    else: 
        print("Ernesti tuli näkyviin")
    

# Button
button = tk.Button(
                tomaatinheitinIkkuna, 
                text="Show Ernesti",
                command=show_ernesti,
                activebackground="black",
                activeforeground="White",
                anchor="s",
                bd=3,
                bg="lightgray",
                cursor="hand2",
                   
disabledforeground=
                "gray",
                fg="black",
                font=("Arial", 12),
                height=2,
                    
highlightbackground=
                "black",
                highlightcolor="green",
                highlightthickness=2,
                justify="center",
                overrelief="raised",
                padx=5,
                pady=1,
                width=15,
                wraplength=100
            )

button.grid(row=2, column=1, sticky="s")

tomaatinheitinIkkuna.mainloop()