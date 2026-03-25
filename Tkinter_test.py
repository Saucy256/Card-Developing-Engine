import tkinter as tk

def WindowStartForGen():
    #create window
    root = tk.Tk()

    # Name of Window
    root.title("Card Generator Definer")

    # Window Size
    root.geometry("1000x750")

    # Locationary Variables
    IntroTitle = [110, 40]

    # Prints Text to Window
    label = tk.Label(root, text = "Welcome to the Digital Card Creator.")
    label.place(x = IntroTitle[0], y = IntroTitle[1])
    label = tk.Label(root, text = "This Code is designed to aid and help in the creation of Trading Card Creation for digital games or for eventual printing.")
    label.place(x = IntroTitle[0], y = (IntroTitle[1] + IntroTitle[1]*1))

    # Start Event Loop
    root.mainloop()

WindowStartForGen()
