""" LABEL
    -----
    Create label widgets.
"""


# -------------------------------------------------------------------------------
# 0. IMPORT LIBRARIES
# -------------------------------------------------------------------------------


from tkinter import *


# -------------------------------------------------------------------------------
# 1. CREATE LABEL WIDGETS USING PACK
# -------------------------------------------------------------------------------


# Create the root widget

root_1 = Tk()


# Create the label widgets

label_1 = Label(root_1, text="First Name")
label_2 = Label(root_1, text="Last Name")


# Position the label widgets into the root widget

label_1.pack()
label_2.pack()


# Create the event loop

root_1.mainloop()


# -------------------------------------------------------------------------------
# 2. CREATE LABEL WIDGETS USING GRID
# -------------------------------------------------------------------------------


# Create the root widget

root_2 = Tk()


# Create the label widgets

label_1 = Label(root_2, text="First Name")
label_2 = Label(root_2, text="Last Name")


# Position the label widgets into the root widget

label_1.grid(row=0, column=0)
label_2.grid(row=1, column=0)


# Create the event loop

root_2.mainloop()
