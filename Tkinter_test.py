from tkinter import *
from tkinter import ttk
import os

'''
# Base code for folder creation
# Specify the nested directory structure
nested_directory = "parent_folder/child_folder"

# Attempts to create a nested directory
try:
    os.makedirs(nested_directory)
    print(f"Nested directories '{nested_directory}' created successfully.")
# Cancels file creation under circumstance of that file already existing
except FileExistsError:
    print(f"One or more directories in '{nested_directory}' already exist.")
# Cancels file creation under circumstance that correct permissions have not been granted
except PermissionError:
    print(f"Permission denied: Unable to create '{nested_directory}'.")
# Cancels file creation and gives any other circumstance.
except Exception as e:
    print(f"An error occurred: {e}")
'''

# Finds size of computer screen for window creation.
size = os.get_terminal_size()

def WindowStartForGen():
    #create window
    root = Tk()
    

    # Name of Window
    root.title("Card Generator Definer")

    # Window Size
    root.geometry("960x540")

    # Locationary Variables
    IntroTitle = [110, 40]

    # Prints Text to Window
    label = Label(root, text = "Welcome to the Digital Card Creator.")
    label.place(x = IntroTitle[0], y = IntroTitle[1])
    label = Label(root, text = "This Code is designed to aid and help in the creation of Trading Card Creation for digital games or for eventual printing.")
    label.place(x = IntroTitle[0], y = (IntroTitle[1] + IntroTitle[1]*1))

    # Copy Names of files from Deck_List
    deck_options = []
    for deck in os.listdir("Deck_List"):
            # Prints file names present Deck_List folder
            deck_options.append(deck) # add to list
    deck_options.append("+ New Deck")

    def selected(event):
        #selectDeck = Label(root, text=clicked.get()).pack()
        if clicked.get() == "+ New Deck":
            selectDeck = Label(root, text="Creating new Deck folder.").pack()
        else:
            selectDeck = Label(root, text=f'The Deck selected was {clicked.get().pack()}.').pack()
    
    clicked = StringVar()
    clicked.set(deck_options[0])

    drop = OptionMenu(root, clicked, *deck_options, command=selected)
    drop.pack(pady=20)

    # myButton = Button(root, text"", command=selected)

    # Start Event Loop
    root.mainloop()

WindowStartForGen()
