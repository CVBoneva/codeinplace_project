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
from delivery_class import DeliveryItems

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600

def main():

    file_name = input("Please enter a file name to load data:")
    print(file_name)
    
    #load data to be displayed  
    #get all destination items, sorted by street name (group
    delivery_items = DeliveryItems(file_name)
    delivery_items.matrix.sort(key = delivery_items.SortFunction)

    # Create the main window
    master = create_widget(None, tk.Tk)
    master.title(delivery_items.title)

    #Create canvas widget
    canvas = create_widget(master, tk.Canvas, bg="dark gray", width=CANVAS_WIDTH, height = CANVAS_HEIGHT)
    canvas.pack(fill="both", expand=True)

    #generate ui 
    create_view(canvas, delivery_items)


    #wait the user to close the window
    canvas.mainloop()


if __name__ == '__main__':
    main()    