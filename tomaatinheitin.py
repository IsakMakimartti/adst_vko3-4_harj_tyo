import tkinter as tk
import random
from tkinter import PhotoImage
import csv
import winsound
from tkinter import *

# Create the main window
tomaatinheitinIkkuna = tk.Tk()
tomaatinheitinIkkuna.title("Tomaatinheitin")
tomaatinheitinIkkuna.geometry('1920x1080')

# Initializing parameters
onkoPainettu = False
row_Ernesti = random.randint(2, 6)
row_Kernesti = random.randint(2, 6)
row_maalitaulu = 4
column_Ernesti = 8
column_Kernesti = 0
column_Maalitaulu = 4
imageTomaatti = PhotoImage(file="tomaatti.png")

# Kernestis Image
imageKernesti = PhotoImage(file="kerne.png")
imageLabelKernesti = tk.Label(tomaatinheitinIkkuna, image=imageKernesti)
imageLabelKernesti.place(x=column_Kernesti * 220, y=row_Kernesti * 100) 

# Maalitaulu Image
imageMaalitaulu = PhotoImage(file="maalitaulu.png")
imageLabelMaalitaulu = tk.Label(tomaatinheitinIkkuna, image=imageMaalitaulu)
imageLabelMaalitaulu.place(relx=0.5, rely=0.5, anchor="center")

imageErnesti = PhotoImage(file="erne.png")
imageLabelErnesti = tk.Label(tomaatinheitinIkkuna, image=imageErnesti)

# Scoreboard
scoreboard = Frame(tomaatinheitinIkkuna)
scoreboard.place(relx=0.5, rely=0.5, anchor="center")

# Ernestis Image
def image_ernesti():
    global row_Ernesti, column_Ernesti
    imageLabelErnesti.image = imageErnesti 
    imageLabelErnesti.place(x=column_Ernesti * 220, y=row_Ernesti * 100) 

def show_ernesti():
    global onkoPainettu, row_Ernesti
  
    if not onkoPainettu:
        image_ernesti()
        print("Ernesti tuli näkyviin!")
        onkoPainettu = True
    else: 
        row_Ernesti = random.randint (2, 6)
        image_ernesti()
       
# Tomato throw functionality
def tomato_shooter_start(
        start_row, 
        start_column, 
        target_row, 
        target_column, 
        target_columnErnesti,
        target_columnKernesti, 
        who_is_shooting
        ):
    print("tomato_shooter pressed!")

    tomaatti = tk.Label(tomaatinheitinIkkuna, image=imageTomaatti, bg='#f7f6f6')
    tomaatti.place(x=start_column * 220, y=start_row * 120) 

    def tomato_move():
        nonlocal start_row, start_column, target_row, target_column
        movement_Rate = 0.5
        movementDelay = 50

        # Check who is shooting and move tomato horizontally
        if who_is_shooting == True:
            if start_column < target_columnErnesti:
                start_column += movement_Rate
            elif start_column > target_columnErnesti:
                start_column -= movement_Rate
        else:
            if start_column < target_columnKernesti:
                start_column += movement_Rate
            elif start_column > target_columnKernesti:
                start_column -= movement_Rate

        tomaatti.place(x=start_column * 220, y=start_row * 120)

        # Check who is shooting and if tomato hits goal, otherwise keep moving horizontally and destroy.
        if who_is_shooting == True:
            if start_column == target_column and start_row == target_row:
                print("Kernesti osui maaliin!")
                winsound.Beep(400, 200)
                field_names = ['Name', 'Status']
                data = [{'Name': 'Kernesti', 'Status': 'Osui'}]
                with open ('Stats.csv', 'a', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=field_names)

                    isFileEmpty = csvfile.tell() == 0
                    if isFileEmpty:
                         writer.writeheader()
  
                    writer.writerows(data)
                scoreKernesti.set(readKernestiData())
                tomaatti.destroy()
            elif start_column != target_columnErnesti:
                tomaatinheitinIkkuna.after(movementDelay, tomato_move)
            elif start_column == column_Ernesti and start_row == row_Ernesti:
                print("Kernesti osui Ernestiin")
                winsound.Beep(900, 200)
                tomaatti.destroy()
                # Ernesti shoots back at Kernesti
                tomato_shooter_start(
                    start_row=row_Ernesti, 
                    start_column=column_Ernesti, 
                    target_row=row_maalitaulu, 
                    target_column=column_Maalitaulu,
                    target_columnErnesti=column_Ernesti,
                    target_columnKernesti=column_Kernesti,
                    who_is_shooting=False
                )
                print("Ernesti ampuu takaisin")
            else:
                tomaatti.destroy()
        else: 
            if start_column == target_column and start_row == target_row:
                print("Ernesti osui maaliin!")
                winsound.Beep(400, 200)
                field_names = ['Name', 'Status']
                data = [{'Name': 'Ernesti', 'Status': 'Osui'}]
                with open ('Stats.csv', 'a', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=field_names)

                    isFileEmpty = csvfile.tell() == 0
                    if isFileEmpty:
                         writer.writeheader()

                    writer.writerows(data)
                scoreErnesti.set(readErnestiData())
                tomaatti.destroy()
            elif start_column != target_columnKernesti:
                tomaatinheitinIkkuna.after(movementDelay, tomato_move)
            else:
                tomaatti.destroy()
    
    tomato_move()

# Buttons for shooting tomatos
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
buttonShowErnesti.place(relx=0.5, rely=0.9, anchor="center") 

buttonShootErnesti = tk.Button(
    tomaatinheitinIkkuna, 
    text="Ernesti",
    command=lambda: tomato_shooter_start(
        start_row=row_Ernesti, 
        start_column=column_Ernesti, 
        target_row=row_maalitaulu, 
        target_column=column_Maalitaulu,
        target_columnErnesti=column_Ernesti,
        target_columnKernesti=column_Kernesti,
        who_is_shooting=False
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
buttonShootErnesti.place(relx=0.6, rely=0.1, anchor="center")

buttonShootKernesti = tk.Button(
    tomaatinheitinIkkuna, 
    text="Kernesti",
    command=lambda: tomato_shooter_start(
        start_row=row_Kernesti, 
        start_column=column_Kernesti, 
        target_row=row_maalitaulu, 
        target_column=column_Maalitaulu,
        target_columnErnesti=column_Ernesti,
        target_columnKernesti=column_Kernesti,
        who_is_shooting=True
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
buttonShootKernesti.place(relx=0.4, rely=0.1, anchor="center")

# Reset functionality and button
def resetData():
    with open ('Stats.csv', 'w', newline='') as emptyFile:
        emptyFile.truncate()
    
    scoreKernesti.set(readKernestiData())
    scoreErnesti.set(readErnestiData())

buttonReset = tk.Button(
    tomaatinheitinIkkuna, 
    text="Reset",
    command=lambda: resetData(),
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
buttonReset.place(relx=0.5, rely=0.71, anchor="center")

# Read score data for Ernesti and Kernesti
def readKernestiData():
    with open('Stats.csv', newline='') as fileKernesti:
        reader = csv.DictReader(fileKernesti)
        # Name column
        column_index = 'Name'
        name = 'Kernesti'
        counter = 0

        for row in reader:
            if row[column_index] == name:
                counter += 1
    return counter

def readErnestiData():
    with open('Stats.csv', newline='') as fileErnesti:
        reader = csv.DictReader(fileErnesti)
        # Name column
        column_index = 'Name'
        name = 'Ernesti'
        counter = 0

        for row in reader:
            if row[column_index] == name:
                counter += 1
    return counter

scoreKernesti = tk.StringVar()
scoreKernesti.set(readKernestiData())

# Labels
labelScoreKernesti = tk.Label(
    tomaatinheitinIkkuna,
    textvariable=scoreKernesti,
    anchor=tk.CENTER,
    bg="lightgray",
    height=3,
    width=10,
    font=("Arial", 16, "bold"),
    cursor="hand2",
    fg="black",
    padx=15,
    pady=15,
    justify=tk.CENTER,
    relief=tk.RAISED,
    underline=0,
    wraplength=250
)

labelScoreKernesti.place(relx=0.46, rely=0.3, anchor="center")

scoreErnesti = tk.StringVar()
scoreErnesti.set(readErnestiData())

labelScoreErnesti = tk.Label(
    tomaatinheitinIkkuna,
    textvariable=scoreErnesti,
    anchor=tk.CENTER,
    bg="lightgray",
    height=3,
    width=10,
    font=("Arial", 16, "bold"),
    cursor="hand2",
    fg="black",
    padx=15,
    pady=15,
    justify=tk.CENTER,
    relief=tk.RAISED,
    underline=0,
    wraplength=250
)

labelScoreErnesti.place(relx=0.54, rely=0.3, anchor="center")

# Reset data and start program
resetData()
tomaatinheitinIkkuna.mainloop()