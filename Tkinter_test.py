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
    
    
    editorMenu = Menu(root)
    root.config(menu=editorMenu)

    def our_command():
        pass
    
    file_Menu = Menu(editorMenu)
    editorMenu.add_cascade(Label="File", menu=file_Menu)
    file_Menu.add_command(Label="New...", command=root.our_command)
    file_Menu.add_separator()
    file_Menu.add_command(Label="Exit", command=root.quit)


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
            deck_options.append(deck)
    # Adds '+ New Deck' button to Deck_List, allowing for adding of decks.
    deck_options.append("+ New Deck")

    def editorsMenu(y=False, n=False):
        if y == True:
            selectDeck = Label(root, text="Opening the Deck folder.").pack()
        elif n == True:
            selectDeck = Label(root, text="Cancelling opening of the Deck folder.").pack()

    def selected(event):
        #selectDeck = Label(root, text=clicked.get()).pack()
        if clicked.get() == "+ New Deck":
            selectDeck = Label(root, text="Creating a new Deck folder.").pack()
        else:
            selectDeck = Label(root, text=f'The Deck selected was {clicked.get()}. Would you like to confirm?').pack()
            confirmDeck = Button(root, text="Confirm Deck", command=editorsMenu)
            confirmDeck.pack()

    
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

WindowStartForGen()
