import tkinter as tk
from tkinter import PhotoImage

tomaatinheitinIkkuna = tk.Tk()

tomaatinheitinIkkuna.title("Tomaatinheitin")
tomaatinheitinIkkuna.geometry('1200x900')

#lbl = tk.Label(tomaatinheitinIkkuna, text="Tomaatinheitin")
#lbl.grid()

# Kernesti
imageKernesti = PhotoImage(file="kerne.png")
imageLabelKernesti = tk.Label(tomaatinheitinIkkuna, image=imageKernesti)
imageLabelKernesti.grid(row=0, column=0)

# Maalitaulu
imageMaalitaulu = PhotoImage(file="maalitaulu.png")
imageLabelMaalitaulu = tk.Label(tomaatinheitinIkkuna, image=imageMaalitaulu)
imageLabelMaalitaulu.grid(row=0, column=1)

tomaatinheitinIkkuna.mainloop()