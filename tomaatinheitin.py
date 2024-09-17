import tkinter as tk
import random
from tkinter import *

tomaatinheitinIkkuna = tk.Tk()

tomaatinheitinIkkuna.title("Tomaatinheitin")
tomaatinheitinIkkuna.geometry('1920x1080')

# Configuration for grid layout
tomaatinheitinIkkuna.grid_rowconfigure(0, weight=0)
tomaatinheitinIkkuna.grid_columnconfigure(0, weight=1)

tomaatinheitinIkkuna.grid_rowconfigure(1, weight=0)
tomaatinheitinIkkuna.grid_columnconfigure(1, weight=0)

tomaatinheitinIkkuna.grid_rowconfigure(2, weight=1)
tomaatinheitinIkkuna.grid_columnconfigure(2, weight=1)

tomaatinheitinIkkuna.grid_rowconfigure(3, weight=0)
tomaatinheitinIkkuna.grid_columnconfigure(3, weight=0)


tomaatinheitinIkkuna.grid_rowconfigure(4, weight=0)
tomaatinheitinIkkuna.grid_columnconfigure(4, weight=1)

onkoPainettu = False
position_Ernesti = random.randint(0, 4)
position_Kernesti = random.randint(0, 4)
imageTomaatti = PhotoImage(file="tomaatti.png")

# Kernestis Image
imageKernesti = PhotoImage(file="kerne.png")
imageLabelKernesti = tk.Label(tomaatinheitinIkkuna, image=imageKernesti)
imageLabelKernesti.grid(row=position_Kernesti, column=0, sticky="w")

# Maalitaulu Image
imageMaalitaulu = PhotoImage(file="maalitaulu.png")
imageLabelMaalitaulu = tk.Label(tomaatinheitinIkkuna, image=imageMaalitaulu)
imageLabelMaalitaulu.grid(row=1, column=2)

# Ernestis Image
def image_ernesti():
    global position_Ernesti
    imageErnesti = PhotoImage(file="erne.png")
    imageLabelErnesti = tk.Label(tomaatinheitinIkkuna, image=imageErnesti)
    imageLabelErnesti.image = imageErnesti 
    imageLabelErnesti.grid(row=position_Ernesti, column=4, sticky="e")

def show_ernesti():
    global onkoPainettu
    if onkoPainettu == False:
        image_ernesti()
        onkoPainettu = True
    else: 
        print("Ernesti tuli näkyviin!")

def tomato_shooter():
    print("tomato_shooter pressed!")
    tomaatti = tk.Label(tomaatinheitinIkkuna, image=imageTomaatti, bg='#f7f6f6')
    tomaatti.grid(row=position_Ernesti, column=4)

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

button.grid(row=4, column=2, sticky="s")

# Button
button2 = tk.Button(
                tomaatinheitinIkkuna, 
                text="Shoot",
                command=tomato_shooter,
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

button2.grid(row=0, column=2, sticky="n")

tomaatinheitinIkkuna.mainloop()