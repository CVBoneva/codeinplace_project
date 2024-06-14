"""
This library contains graphic methods displaying diffrent forms used in the ui
"""
import tkinter as tk
from idlelib.tooltip import Hovertip
import random

FRAME_OFFSET = 20

#creates single widget/form of tkinter types as frame, button, label
def create_widget(parent, widget_type, **options):
    return widget_type(parent, **options)

#creates individual frame, where a table would be nested. i: column number on the screen; j: row number
def create_frame(parent, frame_height, frame_width, i, j):

    bg = get_random_color()
    frame = create_widget(parent, tk.Frame, bg=bg, bd=3, 
                        highlightcolor='red', highlightthickness=2, highlightbackground='black', 
                        width = frame_width, height = frame_height)
    
    frame_padx = FRAME_OFFSET + frame_width * j + FRAME_OFFSET * j
    frame_pady = FRAME_OFFSET + frame_height * i + FRAME_OFFSET * i
    frame.place(x = frame_padx, y = frame_pady, width = frame_width, height = frame_height)
    frame.grid_propagate(0)

    return frame

def get_random_color():
    colors = ["#ffc100", "#ff9a00", "#ff7400", "#ff4d00", "#df699f", "#eda226", "#df97ff"]
    color =random.choice(colors)
    return color

#tooltip box with full address, shown over the name (first table column)
def create_tooltip(parent, text):
    Hovertip(anchor_widget=parent,text=text,hover_delay=None)


FONT_SIZE_TITLE = 16
FONT_SIZE_ROW = 14

WIDTH_COL_BUTTON_LIT = 2
HEIGHT_ROW_LIT = 1

STR_TITLE_FORMAT = "{}  ({})"

STR_ALL_DONE = "All good!"
#creates single table containing the group of items - rows with names and a button
def make_table(parent, street, addresses, name_width, all_gelivery_items, table_title, done_action):

    

    global number_not_delivered 
    number_not_delivered = all_gelivery_items
    #how manu address per current street
    rows = len(addresses)

    STR_TITLE_STATUS = "{} " + table_title
    title = create_title(street, rows, parent, STR_TITLE_STATUS)

    #make table grid
    for r in range(rows):

        name = addresses[r]["name"]
        address = addresses[r]["address"]
        label = create_first_column(parent, name, address, r, name_width)
   
        button = create_second_column(parent, label, r, title, street, done_action, STR_TITLE_STATUS)
   
        parent.columnconfigure(0, weight=name_width)
        parent.columnconfigure(1, weight=WIDTH_COL_BUTTON_LIT)
       

    return


def create_button(parent, text, fg, label, width, height):

    button = create_widget(parent, tk.Button, text=text, fg=fg, bg='lightblue', bd=3, cursor='hand2',
                         highlightcolor='red', highlightthickness=2, highlightbackground='black', 
                         relief=tk.RAISED, height=height, width=width)    
    return button

def create_title(street, rows, parent, STR_TITLE_STATUS):
    #title of the table
    
    title_text = STR_TITLE_FORMAT.format(street, STR_TITLE_STATUS.format(rows))
    title_width = len(title_text)

    title = create_widget(parent, tk.Label, text=title_text, font=("Arial", FONT_SIZE_TITLE, "bold"), bg='lightblue', bd=3, 
                        highlightcolor='red', highlightbackground='black', justify=tk.CENTER, width=title_width)
    title.grid(row = 0,column = 0, columnspan = 2, pady = 15)

    return title

def create_first_column(parent, name, address, r, name_width):
     
    label = create_widget(parent, tk.Label, text=name, font=("Arial", FONT_SIZE_ROW), bg='lightblue', bd=3, 
                    highlightcolor='red', highlightthickness=1, highlightbackground='black', width=name_width, 
                    height=HEIGHT_ROW_LIT)

    label.grid(row=r+1, column=0, padx = 5, pady = 5)
    create_tooltip(label, address)

    return label

def create_second_column(parent, label, r, title, street_name, done_action, STR_TITLE_STATUS):

    def mark_done(event, label, parent):
        label["fg"] = "dark gray"
        event.widget.destroy() 

        label_done = create_widget(parent, tk.Label, text=done_action, font=("Arial", FONT_SIZE_ROW), bg='lightblue', bd=3)
        label_done.grid(row=r+1, column=1, padx = 5, pady = 5)

        change_title(parent, title, street_name, STR_TITLE_STATUS)

    
    button = create_button(parent, text="OK", fg="green", label=label, width=WIDTH_COL_BUTTON_LIT, height=HEIGHT_ROW_LIT)
    button.bind("<Button-1>", lambda event, label=label, parent=parent :mark_done(event, label, parent))
    button.grid(row=r+1, column=1, padx = 5, pady = 5)

    return button


def change_title(frame, title, street_name, STR_TITLE_STATUS):

    children = frame.winfo_children()
    def button_lambda(a):  
        return lambda a: a == "button"  
    
    def get_all_buttons(children):

        is_button = button_lambda("")
        y = 0
        for a in children:
            y += 1 if is_button(a.widgetName) else 0

        return y  
    n = get_all_buttons(children)
    global number_not_delivered
    if n == 0:
        title["text"] = STR_TITLE_FORMAT.format(street_name, STR_ALL_DONE)
    else:        
        title["text"] = STR_TITLE_FORMAT.format(street_name, STR_TITLE_STATUS.format(n))
    
    number_not_delivered-=1

    if number_not_delivered == 0:
        game_over(frame)
 
    return  

def game_over(frame):
    masterName = frame.winfo_parent()
    master = frame._nametowidget(masterName)

    msg = tk.Label(master, text = "You are ready for the next task!", bg='lightgreen', font=('times', 30, 'italic'), wraplength=300)
    msg.pack(fill= tk.BOTH, pady=200, padx=200)

