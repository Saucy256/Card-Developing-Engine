from ast import Set
import os.path
from ssl import Options
from tkinter import *
from tkinter import ttk
import os

### Global Variables Used ###
# Card Type Drop Down
global CardTypeDD
# Card Deck Being Edited
global DeckEdited
# Path to get to Deck chosen
global Deck_Path
# Path to get to Path chosen in deck
global Type_Path
# Name of Type name being assigned
global TypeNameEntry
# Deck Selection Drop Down
global DeckSelectorDD
# Creates loop for Name
global ValidName
# List of Decks
global Deck_Options
# List of Types
global Type_Options
# 
global NewTypeEntry
global EntryLoop
global SetParameters





# Creates Initialization window
def CreateInitializationWindow():
    XofMainGen = 960
    YofMainGen = 540  
    # Create window for main root following the "Initialization" window
    def CreateMainGenWindow():
        # Create overlay window for viewing the 
        def CardViewScreen():
            # Set Root
            SubWin = Toplevel()
        
            # Name of Window
            SubWin.title(f'{CardTypeDD.get()} Deck Editor')

            # Window Size
            SubWin.geometry(f'{XofMainGen}x{YofMainGen}')


            # Locationary Variables
            IntroTitle = [XofMainGen/8, YofMainGen/10]

        # Close Original Root and Set New
        Initialized.withdraw()
        Editor = Toplevel()
        

        # Pull Deck Selected from Initialization Tab
        DeckEdited = (f'{DeckSelectorDD.get()}')

        # Create File path to Main Deck Card
        Deck_Path = (f'{os.getcwd()}\\Deck_List\\{DeckEdited}\\')
        
        
        # Name of Window
        Editor.title(f'{DeckEdited} Deck Editor')

        # Window Size
        Editor.geometry(f'{XofMainGen}x{YofMainGen}')


        # Locationary Variables
        IntroTitle = [XofMainGen/8, YofMainGen/10]

        def CardTypeCreator():
            NoType = Label(Editor, text="Please Enter the name of the new 'Type' you'd like to create.").pack()
            #Starts loop for valid type name
            ValidName = False
            while(ValidName == False):
                def GetName(event):
                    # If Typing is completed with an empty name, the code bounces back a response.
                    global TypeNameEntry
                    TypeNameEntry = event
                    if TypeNameEntry == "" or TypeNameEntry == " + New Type":
                        Label(Editor, text=f'New type name invalid. Please try again.')
                    else:
                        Label(Editor, text=f'New Type Named {TypeNameEntry} is being created...').pack()
                        global ValidName
                        ValidName = True
                # Requests user input to create new 'Type' name
                global NewTypeEntry
                NewTypeEntry = Entry(Editor, width=30)
                NewTypeEntry.pack()
                global TypeEntry
                TypeEntry = StringVar(value="")
                # Waits for button and submits Entry Name
                SubmitTypeName = Button(Editor, text="Submit Name", command=lambda: TypeEntry.set(NewTypeEntry.get()))
                SubmitTypeName.pack()
                SubmitTypeName.wait_variable(TypeEntry)
                GetName(TypeEntry)

                
          
            # Path to Card File
            CardTypeFolder = f'CardType_{NewTypeEntry.get}'
            # Specify the nested directory structure
            global CardTypes
            CardTypes = (f'{Deck_Path}{CardTypeFolder}')

            # Verifies Existance of Card Type directory
            try:
                os.makedirs(CardTypes)
                print(f"Nested directories '{CardTypes}' created successfully.")
            # Cancels file creation under circumstance of that file already existing
            except FileExistsError:
                print(f"Necessary folder '{CardTypes}' already exist.")
            # Cancels file creation under circumstance that correct permissions have not been granted
            except PermissionError:
                print(f"Permission denied: Unable to create '{CardTypes}'.")
            # Cancels file creation and gives any other circumstance.
            except Exception as e:
                print(f"An error occurred: {e}")


        def CardView(event):
            global SelectedType
            SelectedType = event
            if SelectedType == " + New Type":
                CardTypeCreator()
            else:
                Label(Editor, text=f'The type of card you decided to view was: {SelectedType}')
                Label(Editor, text="Opening seperate window to view cards....")
                CardViewScreen(SelectedType)

        def SetType():
            Type_Options.clear()
            ConfirmedType = False
            while ConfirmedType == False:
                # Copy Names of files from Deck_List
                if len(os.listdir(f'{Deck_Path}')) == 0:
                    CardTypeCreator()
                else:
                    
                    for Dtype in os.listdir(f'{DeckEdited}'):
                        # Prints file names present Deck_List folder
                        Type_Options.append(Dtype)
                    # Adds '+ New Deck' button to Deck_List, allowing for adding of decks.
                    Type_Options.append(" + New Type")
                    # Creates Drop Down Button for selecting card type to be edited
                    global CardTypeDD
                    CardTypeDD = StringVar()
                    CardTypeDD.set(Type_Options[0])

                    # Creates drop down menu for interactions
                    drop = OptionMenu(Editor, CardTypeDD, *Type_Options, command=CardView(CardTypeDD.get()))
                    drop.pack(pady=20)
                    




        # Specify the nested directory structure
        Type_Options = []
        SetParameters = False
        while SetParameters == False:
            SetType()
            CardTypeCreator()
        
        
        mainloop()
    

    # Root Title
    Initialized = Tk()
    
    
    # Name of Window
    Initialized.title("Initialize Card Generator")


    # Window Size
    Initialized.geometry("960x540")


    # Locationary Variables
    IntroTitle = [XofMainGen/8, YofMainGen/10]


    # Prints Text to Window
    label = Label(Initialized, text = "Welcome to the Digital Card Creator.")
    label.pack()
    label = Label(Initialized, text = "This Code is designed to aid and help in the creation of Trading Card Creation for digital games or for eventual printing.")
    label.pack()


    # Copy Names of files from Deck_List
    Deck_Options = []

    for deck in os.listdir("Deck_List"):
            # Prints file names present Deck_List folder
            Deck_Options.append(deck)

    # Adds '+ New Deck' button to Deck_List, allowing for adding of decks.
    Deck_Options.append(" + New Deck")
    
    # Create Window for creating deck folders.
    def DeckCreationWindow():

        # Defines the 'Root' title and 'Window' title
        DeckCreator = Toplevel()
        DeckCreator.title("Deck Creator")


        # Determines width of screen
        XofCreationWin = 960

        # Determines Height of Screen
        YofCreationWin = 540


        # Uses X and Y to Define Size
        DeckCreator.geometry(f'{XofCreationWin}x{YofCreationWin}')


        # Type Name of deckcard
        ValidName = False
        while ValidName == False:
            NewDeckName = Entry(DeckCreator, width=30)
            NewDeckName.pack(pady=20)
            if NewDeckName == "":
                Label(DeckCreator, text="Deck Name invalid. Please try again.")
            else:
                Label(Initialized, text=f'New Deck Named{NewDeckName.get()} is being created...').pack()
               
        # Runs event loop for Creation Window
        mainloop()



    # Uses "Confirm Creation" button to build a new folder path
    def ConfirmFolderCreation():
        selectDeck = Label(Initialized, text="Please type the name of your deck.").pack()
        # Opens Editor Window
        DeckCreationWindow()  


    # Uses "Cancel Creation" button to close menu and restart file initialization process
    def CancelFolderCreation():
        selectDeck = Label(Initialized, "Cancelling.").pack()
        selectDeck = Label(Initialized, "Please Select a new Deck").pack()


    # Uses "Confirm Selection" button to open a folder path to selected Deck's folder
    def ConfirmDeckSelection():
        selectDeck = Label(Initialized, text="Opening the Deck folder.").pack()
        # Opens Main Window
        CreateMainGenWindow()


    # Uses "Cancel Selection" button to close menu and restart file initialization process
    def CancelDeckSelection():
        selectDeck = Label(Initialized, text="Cancelling.").pack()
        selectDeck = Label(Initialized, text="Please Select a new Deck").pack()


    # Defines the even assigned to the drop down window for selecting a Deck
    def selected(event):
        DisplayDeckName = Label(Initialized, text=DeckSelectorDD.get()).pack()

        if DeckSelectorDD.get() == " + New Deck":
            selectDeck = Label(Initialized, text="Please confirm you would like to create a new Deck folder.").pack()
            ConfirmCreation = Button(Initialized, text="Confirm Deck Creation", command=ConfirmFolderCreation)
            ConfirmCreation.pack()
            CancelCreation = Button(Initialized, text="Cancel Deck Creation", command=CancelFolderCreation)
            CancelCreation.pack()

        else:
            selectDeck = Label(Initialized, text=f'The Deck selected was {DeckSelectorDD.get()}. Would you like to confirm?').pack()
            ConfirmSelection = Button(Initialized, text="Confirm Deck Selection", command=ConfirmDeckSelection)
            ConfirmSelection.pack()
            CancelSelection = Button(Initialized, text="Cancel Deck Selection", command=CancelDeckSelection)
            CancelSelection.pack()

           
    DeckSelectorDD = StringVar()
    DeckSelectorDD.set(Deck_Options[0])


    # Creates drop down menu for interactions
    drop = OptionMenu(Initialized, DeckSelectorDD, *Deck_Options, command=selected)
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
