""" BUTTON
    ------
    Create button widgets.
"""


# -------------------------------------------------------------------------------
# 0. IMPORT LIBRARIES
# -------------------------------------------------------------------------------


from tkinter import *


# -------------------------------------------------------------------------------
# 1. CREATE A BUTTON WIDGET
# -------------------------------------------------------------------------------


# Create the root widget

root_1 = Tk()


# Associate a function with a button

def click_1():

    label_1 = Label(root_1, text="Result of click_1")
    label_1.grid(row=0, column=0)


# Create the button widget

button_1 = Button(root_1, text="Compute", padx=30, pady=10, fg="blue", command=click_1)


# Position the button widget into the root widget

button_1.grid(row=0, column=0)


# Create the event loop

root_1.mainloop()
