import tkinter as tk
import random
from tkinter import *

tomaatinheitinIkkuna = tk.Tk()
tomaatinheitinIkkuna.title("Tomaatinheitin")
tomaatinheitinIkkuna.geometry('1920x1080')

# Configuration for grid layout
for i in range(9):
    tomaatinheitinIkkuna.grid_rowconfigure(i, weight=0)
    tomaatinheitinIkkuna.grid_columnconfigure(i, weight=0)

# Fix Maalitaulu
    tomaatinheitinIkkuna.grid_rowconfigure(4, weight=1)
    tomaatinheitinIkkuna.grid_columnconfigure(4, weight=1)

# Initializing parameters
onkoPainettu = False
row_Ernesti = random.randint(0, 8)
row_Kernesti = random.randint(0, 8)
row_maalitaulu = 4
column_Ernesti = 8
column_Kernesti = 0
column_Maalitaulu = 4
imageTomaatti = PhotoImage(file="tomaatti.png")

# Kernestis Image
imageKernesti = PhotoImage(file="kerne.png")
imageLabelKernesti = tk.Label(tomaatinheitinIkkuna, image=imageKernesti)
imageLabelKernesti.grid(row=row_Kernesti, column=column_Kernesti, sticky="w")

# Maalitaulu Image
imageMaalitaulu = PhotoImage(file="maalitaulu.png")
imageLabelMaalitaulu = tk.Label(tomaatinheitinIkkuna, image=imageMaalitaulu)
imageLabelMaalitaulu.grid(row=row_maalitaulu, column=column_Maalitaulu, sticky="nsew")

# Ernestis Image
def image_ernesti():
    global row_Ernesti, column_Ernesti
    imageErnesti = PhotoImage(file="erne.png")
    imageLabelErnesti = tk.Label(tomaatinheitinIkkuna, image=imageErnesti)
    imageLabelErnesti.image = imageErnesti 
    imageLabelErnesti.grid(row=row_Ernesti, column=column_Ernesti, sticky="e")

def show_ernesti():
    global onkoPainettu
    if onkoPainettu == False:
        image_ernesti()
        print("Ernesti tuli näkyviin!")
        onkoPainettu = True
    else: 
        print("Ernesti on jo näkyvissä")

# Tomato throw functionality
def tomato_shooter_start(start_row, start_column, target_row, target_column):
    print("tomato_shooter pressed!")

    tomaatti = tk.Label(tomaatinheitinIkkuna, image=imageTomaatti, bg='#f7f6f6')
    tomaatti.grid(row=start_row, column=start_column)

    def tomato_move():
        nonlocal start_row, start_column
        movement_Rate = 1

        if start_row < target_row:
            start_row += movement_Rate
        elif start_row > target_row:
            start_row -= movement_Rate
        
        if start_column < target_column:
            start_column += movement_Rate
        elif start_column > target_column:
            start_column -= movement_Rate
        
        tomaatti.grid(row=start_row, column=start_column)

        if ( start_column ) != ( target_column ):
            tomaatinheitinIkkuna.after(100 , tomato_move)
        else:
            tomaatti.destroy()

    tomato_move()
    
buttonShowErnesti = tk.Button(
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

buttonShowErnesti.grid(row=8, column=4, sticky="s")

buttonShootErnesti = tk.Button(
                tomaatinheitinIkkuna, 
                text="Ernesti",
                command=lambda: tomato_shooter_start(
                    start_row=row_Ernesti, 
                    start_column=column_Ernesti, 
                    target_row=row_maalitaulu, 
                    target_column=column_Maalitaulu
                    ),
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

buttonShootErnesti.grid(row=0, column=5, sticky="n")


buttonShootKernesti = tk.Button(
                tomaatinheitinIkkuna, 
                text="Kernesti",
                command=lambda: tomato_shooter_start(
                    start_row=row_Kernesti, 
                    start_column=column_Kernesti, 
                    target_row=row_maalitaulu, 
                    target_column=column_Maalitaulu
                    ),
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

buttonShootKernesti.grid(row=0, column=3, sticky="n")

tomaatinheitinIkkuna.mainloop()