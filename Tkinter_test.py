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





# Creates Initialization window
def CreateInitializationWindow():
    
    # Create window for main root following the "Initialization" window
    def CreateMainGenWindow():
        DeckEdited = clicked.get()
        Initialized.withdraw()
        Editor = Toplevel()
        # Name of Window
        Editor.title(f'{clicked.get()} Deck Editor')

        # Window Size
        Editor.geometry(f'{960}x{540}')


        # Locationary Variables
        IntroTitle = [110, 40]

        editorMenu = Menu
        mainloop()
    
    # Root Title
    Initialized = Tk()
        
    # Name of Window
    Initialized.title("Initialize Card Generator")

    # Window Size
    Initialized.geometry("960x540")


    # Locationary Variables
    IntroTitle = [110, 40]


    # Prints Text to Window
    label = Label(Initialized, text = "Welcome to the Digital Card Creator.")
    label.place(x = IntroTitle[0], y = IntroTitle[1])
    label = Label(Initialized, text = "This Code is designed to aid and help in the creation of Trading Card Creation for digital games or for eventual printing.")
    label.place(x = IntroTitle[0], y = (IntroTitle[1] + IntroTitle[1]*1))


    # Copy Names of files from Deck_List
    deck_options = []
    for deck in os.listdir("Deck_List"):
            # Prints file names present Deck_List folder
            deck_options.append(deck)
    # Adds '+ New Deck' button to Deck_List, allowing for adding of decks.
    deck_options.append("+ New Deck")
    


    # Create Window for creating deck folders.
    def DeckCreationWindow():

        DeckCreator = Toplevel()
        DeckCreator.title("Deck Creator")
        DeckCreator.geometry("400x600")
        mainloop()



    # Uses "Confirm Creation" button to build a new folder path
    def ConfirmFolderCreation():
        selectDeck = Label(Initialized, text="Please type the name of your deck.").pack()
        CreateMainGenWindow()
        Initialized.close()    

    # Uses "Cancel Creation" button to close menu and restart file initialization process
    def CancelFolderCreation():
        selectDeck = Label(Initialized, "Cancelling.").pack()
        selectDeck = Label(Initialized, "Please Select a new Deck").pack()

    # Uses "Confirm Selection" button to open a folder path to selected path
    def ConfirmDeckSelection():
        selectDeck = Label(Initialized, text="Opening the Deck folder.").pack()
        CreateMainGenWindow()
        Initialized.close()  

    # Uses "Cancel Selection" button to close menu and restart file initialization process
    def CancelDeckSelection():
        selectDeck = Label(Initialized, text="Cancelling.").pack()
        selectDeck = Label(Initialized, text="Please Select a new Deck").pack()

    def selected(event):
        selectDeck = Label(Initialized, text=clicked.get()).pack()
        if clicked.get() == "+ New Deck":
            selectDeck = Label(Initialized, text="Please confirm you would like to create a new Deck folder.").pack()
            ConfirmCreation = Button(Initialized, text="Confirm Deck Creation", command=ConfirmFolderCreation)
            ConfirmCreation.pack()
            CancelCreation = Button(Initialized, text="Cancel Deck Creation", command=CancelFolderCreation)
            CancelCreation.pack()
        else:
            selectDeck = Label(Initialized, text=f'The Deck selected was {clicked.get()}. Would you like to confirm?').pack()
            ConfirmSelection = Button(Initialized, text="Confirm Deck Selection", command=ConfirmDeckSelection)
            ConfirmSelection.pack()
            CancelSelection = Button(Initialized, text="Cancel Deck Selection", command=CancelDeckSelection)
            CancelSelection.pack()
    global clicked
    clicked = StringVar()
    clicked.set(deck_options[0])

    # Creates drop down menu for interactions
    drop = OptionMenu(Initialized, clicked, *deck_options, command=selected)
    drop.pack(pady=20)
    
    
    '''
    deck_Select = ttk.Combobox(Initialized, value=deck_options)
    deck_Select.current(0)
    deck_Select.bind("<<ComboboxSelected>>", selected)
    deck_Select.pack()
    '''
    
    
    

    # Start Event Loop
    Initialized.mainloop()

CreateInitializationWindow()
