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
# Sets Loop for confirming deck
global ConfirmingDeck
# Creates loop for Name
global ValidName
# List of Decks
global Deck_Options
# List of Types
global Type_Options
# Defines New Type Entry
global NewTypeEntry
# Type picked from drop down bar
global TypePicked
# Creates Delayed function, allowing the entry to be filled out before the button collects the value
global EntryLoop
# Sets Parameters for 
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
            SubWin.title(f'{CardTypeDD.get()} Deck View')

            # Window Size
            SubWin.geometry(f'{XofMainGen}x{YofMainGen}')


            # Locationary Variables
            IntroTitle = [XofMainGen/8, YofMainGen/10]

        # Close Original Root and Set New
        Initialized.withdraw()
        Editor = Toplevel()

        # destroy all widgets from frame
        def clearWindowEditor():
            for widget in Editor.winfo_children():
               widget.destroy()
        

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
                # If Typing is completed with an empty name, the code bounces back a response.
                if TypeEntry == "" or TypeEntry == " + New Type":
                    Label(Editor, text=f'New type name invalid. Please try again.')
                else:
                    Label(Editor, text=f'New Type Named {TypeEntry.get()} is being created...').pack()
                    ValidName = True

                
          
            # Path to Card File

            CardTypeFolder = TypeEntry.get()
            # Specify the nested directory structure
            global CardTypes
            CardTypes = (f'{Deck_Path}{CardTypeFolder}')

            # Verifies Existance of Card Type directory
            try:
                os.makedirs(CardTypes)
                print(f"Folder '{CardTypes}' created successfully.")
            # Cancels file creation under circumstance of that file already existing
            except FileExistsError:
                print(f"Necessary folder '{CardTypes}' already exist.")
            # Cancels file creation under circumstance that correct permissions have not been granted
            except PermissionError:
                print(f"Permission denied: Unable to create '{CardTypes}'.")
            # Cancels file creation and gives any other circumstance.
            except Exception as e:
                print(f"An error occurred: {e}")

        # View Cards located in selected Type
        def TypeSelectionView():
            global SelectedType
            SelectedType = CardTypeDD.get()
            if SelectedType == " + New Type":
                CardTypeCreator()
            else:
                Label(Editor, text=f'The type of card you decided to view was: {SelectedType}')
                Label(Editor, text="Opening seperate window to view cards....")
                CardViewScreen(SelectedType)
                

        # Runs a series of loops based on a drop down menu. Determines type of card to view.
        def SetType():
            TypeConfirmationLoop = False
            while TypeConfirmationLoop == False:
                clearWindowEditor()
                # Resets upon loop back
                Type_Options.clear()
                # Copy Names of files from Deck_List
                if len(os.listdir(f'{Deck_Path}')) == 0:
                    CardTypeCreator()
                else:
                    for Dtype in os.listdir(f'{Deck_Path}'):
                        # Prints file names present Deck_List folder
                        Type_Options.append(Dtype)
                    # Adds '+ New Deck' button to Deck_List, allowing for adding of decks.
                    Type_Options.append(" + New Type")
                    # Creates Drop Down Button for selecting card type to be edited
                    global CardTypeDD
                    CardTypeDD = StringVar()
                    CardTypeDD.set(Type_Options[0])

                    # Creates drop down menu for interactions
                    drop = OptionMenu(Editor, CardTypeDD, *Type_Options, command=TypeSelectionView)
                    drop.pack(pady=20)
                    global TypePicked 
                    TypePicked = StringVar(value="")
                    # Waits for button and submits Entry Name
                    SubmitTypeName = Button(Editor, text="Click to Continue", command=lambda: TypePicked.set(CardTypeDD.get()))
                    SubmitTypeName.pack()
                    SubmitTypeName.wait_variable(TypePicked)
                    if TypePicked.get() == " + New Type":
                        CardTypeCreator()
                    else:
                        Label(Editor, text=f'{TypePicked.get()} was selected.').pack()
                        TypeConfirmationLoop = True

                    




        # Specify the nested directory structure
        Type_Options = []
        SetParameters = False
        while SetParameters == False:
            SetType()
        
        
        mainloop()
    

    # Root Title
    Initialized = Tk()
    
    
    # Name of Window
    Initialized.title("Initialize Card Generator")


    # Window Size
    Initialized.geometry("960x540")


    # Locationary Variables
    IntroTitle = [XofMainGen/8, YofMainGen/10]

    # destroy all widgets from frame
    def clearWindowInitialized():
        for widget in Initialized.winfo_children():
            widget.destroy()

    # View Cards located in selected Type
    def DeckOptionView():
        global SelectedDeck
        SelectedDeck = DeckSelectorDD.get()
        if SelectedDeck == " + New Type":
            CardDeckCreator()
        else:
            Label(Initialized, text=f'The type of card you decided to view was: {SelectedDeck}')
            Label(Initialized, text="Opening seperate window to view cards....")
            CreateMainGenWindow()

    # Uses "Confirm Creation" button to build a new folder path
    def CardDeckCreator():
        clearWindowInitialized()
        NoType = Label(Initialized, text="Please Enter the name of the new 'Deck' you'd like to create.").pack()
        #Starts loop for valid type name
        ValidName = False
        while(ValidName == False):
            # Requests user input to create new 'Type' name
            global NewDeckEntry
            NewDeckEntry = Entry(Initialized, width=30)
            NewDeckEntry.pack()
            global DeckEntry
            DeckEntry = StringVar(value="")
            # Waits for button and submits Entry Name
            SubmitDeckName = Button(Initialized, text="Submit Name", command=lambda: DeckEntry.set(NewDeckEntry.get()))
            SubmitDeckName.pack()
            SubmitDeckName.wait_variable(DeckEntry)
            # If Typing is completed with an empty name, the code bounces back a response.
            if DeckEntry == "" or DeckEntry == " + New Deck":
                Label(Initialized, text=f'New type name invalid. Please try again.')
            else:
                Label(Initialized, text=f'New Deck Named {DeckEntry.get()} is being created...').pack()
                ValidName = True
            
        # Path to Card File
        CardDeckFolder = DeckEntry.get()
        # Specify the nested directory structure
        global CardDecks
        CardDecks = (f'{os.getcwd()}\\Deck_List\\{CardDeckFolder}')

        # Verifies Existance of Card Type directory
        try:
            os.makedirs(CardDecks)
            print(f"Folder '{CardDecks}' created successfully.")
        # Cancels file creation under circumstance of that file already existing
        except FileExistsError:
            print(f"Necessary folder '{CardDecks}' already exist.")
        # Cancels file creation under circumstance that correct permissions have not been granted
        except PermissionError:
            print(f"Permission denied: Unable to create '{CardDecks}'.")
        # Cancels file creation and gives any other circumstance.
        except Exception as e:
            print(f"An error occurred: {e}")


    # Defines the even assigned to the drop down window for selecting a Deck
    def DeckSelector():
        Deck_Options = []
        DeckSelectionLoop = True
        #while DeckSelectionLoop == True:
        Deck_Options.clear()
        # Copy Names of files from Deck_List
        for deck in os.listdir("Deck_List"):
                # Prints file names present Deck_List folder
                Deck_Options.append(deck)
        # Adds '+ New Deck' button to Deck_List, allowing for adding of decks.
        Deck_Options.append(" + New Deck")
        # Creates drop down menu for selecting what deck your opening
        global DeckSelectorDD
        DeckSelectorDD = StringVar()
        DeckSelectorDD.set(Deck_Options[0])
        drop = OptionMenu(Initialized, DeckSelectorDD, *Deck_Options, command=DeckOptionView)
        drop.pack(pady=20)
        global DeckPicked
        DeckPicked = StringVar(value="")
        # Waits for button and submits Entry Name
        ConfirmSelection = Button(Initialized, text="Confirm", command=lambda: DeckPicked.set(DeckSelectorDD.get()))
        ConfirmSelection.pack()
        ConfirmSelection.wait_variable(DeckPicked)
        DisplayDeckName = Label(Initialized, text=DeckSelectorDD.get()).pack()
        if DeckSelectorDD.get() == " + New Deck":
            CardDeckCreator()
        else:
            # Opens Main Window
            CreateMainGenWindow()

    # Prints Text to Window
    label = Label(Initialized, text = "Welcome to the Digital Card Creator.")
    label.pack()
    label = Label(Initialized, text = "This Code is designed to aid and help in the creation of Trading Card Creation for digital games or for eventual printing.")
    label.pack()
    
    DeckSelector()

    # Start Event Loop
    Initialized.mainloop()

CreateInitializationWindow()
