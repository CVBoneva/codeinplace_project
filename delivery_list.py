"""
Delivery list is a simple application that displays grouped sorted items.
Items are persons with name and address. 
Each group has a common criterion - street. 
Each group consists of items shown in a table, with possibility 
to be marked as finished. 
"""
import tkinter as tk
from widgets import create_widget 
from tables import create_view

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600

def main():
    # Create the main window
    master = create_widget(None, tk.Tk)
    master.title("My delivery list")

    #Create canvas widget
    canvas = create_widget(master, tk.Canvas, bg="dark gray", width=CANVAS_WIDTH, height = CANVAS_HEIGHT)
    canvas.pack(fill="both", expand=True)

    #generate ui 
    create_view(canvas)

    #wait the user to close the window
    canvas.mainloop()


if __name__ == '__main__':
    main()    