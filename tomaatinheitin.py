import tkinter as tk
import random
from tkinter import PhotoImage

# Create the main window
tomaatinheitinIkkuna = tk.Tk()
tomaatinheitinIkkuna.title("Tomaatinheitin")
tomaatinheitinIkkuna.geometry('1920x1080')

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
imageLabelKernesti.place(x=column_Kernesti * 200, y=row_Kernesti * 120) 

# Maalitaulu Image
imageMaalitaulu = PhotoImage(file="maalitaulu.png")
imageLabelMaalitaulu = tk.Label(tomaatinheitinIkkuna, image=imageMaalitaulu)
imageLabelMaalitaulu.place(relx=0.5, rely=0.5, anchor="center") 

# Ernestis Image
def image_ernesti():
    global row_Ernesti, column_Ernesti
    imageErnesti = PhotoImage(file="erne.png")
    imageLabelErnesti = tk.Label(tomaatinheitinIkkuna, image=imageErnesti)
    imageLabelErnesti.image = imageErnesti 
    imageLabelErnesti.place(x=column_Ernesti * 200, y=row_Ernesti * 120) 

def show_ernesti():
    global onkoPainettu
    if not onkoPainettu:
        image_ernesti()
        print("Ernesti tuli näkyviin!")
        onkoPainettu = True
    else: 
        print("Ernesti on jo näkyvissä")

# Tomato throw functionality
def tomato_shooter_start(start_row, start_column, target_row, target_column):
    print("tomato_shooter pressed!")

    tomaatti = tk.Label(tomaatinheitinIkkuna, image=imageTomaatti, bg='#f7f6f6')
    tomaatti.place(x=start_column * 200, y=start_row * 120)  # Adjust placement as needed

    def tomato_move():
        nonlocal start_row, start_column
        movement_Rate = 0.5
        movementDelay = 100

        if start_column < target_column:
            start_column += movement_Rate
        elif start_column > target_column:
            start_column -= movement_Rate
        
        tomaatti.place(x=start_column * 200, y=start_row * 120)  # Adjust placement as needed

        if start_column != target_column:
            tomaatinheitinIkkuna.after(movementDelay, tomato_move)
        else:
            tomaatti.destroy()
    tomato_move()

# Buttons
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
    disabledforeground="gray",
    fg="black",
    font=("Arial", 12),
    height=2,
    highlightbackground="black",
    highlightcolor="green",
    highlightthickness=2,
    justify="center",
    overrelief="raised",
    padx=5,
    pady=1,
    width=15,
    wraplength=100
)
buttonShowErnesti.place(relx=0.5, rely=0.9, anchor="center")  # Centered horizontally at the bottom

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
    disabledforeground="gray",
    fg="black",
    font=("Arial", 12),
    height=2,
    highlightbackground="black",
    highlightcolor="green",
    highlightthickness=2,
    justify="center",
    overrelief="raised",
    padx=5,
    pady=1,
    width=15,
    wraplength=100
)
buttonShootErnesti.place(relx=0.6, rely=0.1, anchor="center")  # Positioned at the top-left

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
    disabledforeground="gray",
    fg="black",
    font=("Arial", 12),
    height=2,
    highlightbackground="black",
    highlightcolor="green",
    highlightthickness=2,
    justify="center",
    overrelief="raised",
    padx=5,
    pady=1,
    width=15,
    wraplength=100
)
buttonShootKernesti.place(relx=0.4, rely=0.1, anchor="center")  # Positioned slightly below the first button

# Run the application
tomaatinheitinIkkuna.mainloop()