from tkinter import *
from tkinter import ttk
import os

# Initalized Variables
root = Tk()

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


# Create Window for main root following the "Initialization" window
def CreateMainGenWindow(DeckSelected):
    # Name of Window
    root.title(f'{DeckSelected} Editor')

    # Window Size
    root.geometry(f'{960}x{540}')


    # Locationary Variables
    IntroTitle = [110, 40]

    editorMenu = Menu


# Creates Initialization window
def CreateInitializationWindow():
    

    # Name of Window
    root.title("Initialize Card Generator")

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
            deck_options.append(deck)
    # Adds '+ New Deck' button to Deck_List, allowing for adding of decks.
    deck_options.append("+ New Deck")
    
    def DeckCreationWindow():

        root.title("Deck Creation")
        root.geometry("400x600")
    # Uses "Confirm Creation" button to build a new folder path
    def ConfirmFolderCreation():
        selectDeck = Label(root, text="Opening the Deck folder.").pack()
        CreateMainGenWindow(clicked.get())
        
        exit("Initialize Card Generator")    

    # Uses "Cancel Creation" button to close menu and restart file initialization process
    def CancelFolderCreation():
        selectDeck = Label(root, "Cancelling.").pack()
        selectDeck = Label(root, "Please Select a new Deck").pack()

    # Uses "Confirm Selection" button to open a folder path to selected path
    def ConfirmDeckSelection(DeckName):
        selectDeck = Label(root, "Opening the Deck folder.").pack()
        CreateMainGenWindow(clicked.get())
        exit("Initialize Card Generator")

    # Uses "Cancel Selection" button to close menu and restart file initialization process
    def CancelDeckSelection():
        selectDeck = Label(root, text="Cancelling.").pack()
        selectDeck = Label(root, text="Please Select a new Deck").pack()

    def selected(event):
        selectDeck = Label(root, text=clicked.get()).pack()
        if clicked.get() == "+ New Deck":
            selectDeck = Label(root, text="Please confirm you would like to create a new Deck folder.").pack()
            ConfirmCreation = Button(root, text="Confirm Deck Creation", command=ConfirmFolderCreation)
            ConfirmCreation.pack()
            CancelCreation = Button(root, text="Cancel Deck Creation", command=CancelFolderCreation)
            CancelCreation.pack()
        else:
            selectDeck = Label(root, text=f'The Deck selected was {clicked.get()}. Would you like to confirm?').pack()
            ConfirmSelection = Button(root, text="Confirm Deck Selection", command=ConfirmDeckSelection)
            ConfirmSelection.pack()
            CancelSelection = Button(root, text="Confirm Deck Selection", command=ConfirmDeckSelection)
            CancelSelection.pack()

    
    clicked = StringVar()
    clicked.set(deck_options[0])

    # Creates drop down menu for interactions
    drop = OptionMenu(root, clicked, *deck_options, command=selected)
    drop.pack(pady=20)
    
    
    '''
    deck_Select = ttk.Combobox(root, value=deck_options)
    deck_Select.current(0)
    deck_Select.bind("<<ComboboxSelected>>", selected)
    deck_Select.pack()
    '''
    
    
    

    # Start Event Loop
    root.mainloop()

CreateInitializationWindow()
