""" WIDGETS
    -------
    Create label, button and entry widgets.
"""


# -------------------------------------------------------------------------------
# 0. IMPORT LIBRARIES
# -------------------------------------------------------------------------------


from tkinter import *


# -------------------------------------------------------------------------------
# 1. CREATE LABEL WIDGETS
# -------------------------------------------------------------------------------


# Create the root widget

root = Tk()


# Create the label widgets and position it into the root widget

label = Label(root, text="First Name")
label.grid(row=0, column=0)


# Create the event loop

root.mainloop()


# -------------------------------------------------------------------------------
# 2. CREATE BUTTON WIDGETS
# -------------------------------------------------------------------------------


# Create the root widget

root = Tk()


# Associate a function with the button widget

def click():

    label = Label(root, text="You pressed the button")
    label.grid(row=1, column=0)


# Create the button widget

button = Button(root, text="Press the button", padx=30, pady=10, command=click)
button.grid(row=0, column=0)


# Create the event loop

root.mainloop()


# -------------------------------------------------------------------------------
# 3. CREATE ENTRY WIDGETS
# -------------------------------------------------------------------------------


# Create the root widget

root = Tk()


# Create the entry widget

entry = Entry(root, width=30)
entry.grid(row=0, column=0)


# Create the event loop

root.mainloop()


# -------------------------------------------------------------------------------
# 4. EXAMPLE 1
# -------------------------------------------------------------------------------


# Create the root widget

root = Tk()


# Create the entry widget

entry = Entry(root)
entry.insert(0, "Name Surname")
entry.grid(row=0, column=0)


# Associate a function with the button

def click():

    label = Label(root, text=entry.get())
    label.grid(row=2, column=0)


# Create the button widget widget

button = Button(root, text="Press to print entry", command=click)
button.grid(row=1, column=0)


# Create the event loop

root.mainloop()


# -------------------------------------------------------------------------------
# 4. EXAMPLE 2
# -------------------------------------------------------------------------------

