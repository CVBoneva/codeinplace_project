from delivery_class import DeliveryItems
import math
from widgets import create_frame, make_table 

NUM_WIDGETS_PER_LINE = 4
WIDTH_PER_SYMBOL_PX = 10
HEIGHT_PER_ROW_PX = 70

def create_view(parent, delivery_items):

    #
    (h_block, w_block, sorted_array, longest_name) = make_calculations_and_possitioning(delivery_items)
    all_gelivery_items = len(delivery_items.matrix)   

    table_title_action = delivery_items.to_do_action
    button_done_action = delivery_items.finished_action
    #creates each table in grid - starting left-top WE (left to right)(row 0, col 0)(row 0, col 1) ...
    i = 0
    for k in sorted_array.keys():
        addresses = sorted_array[k]
        grid_row = i // NUM_WIDGETS_PER_LINE
        grid_col = i % NUM_WIDGETS_PER_LINE

        frame = create_frame(parent, h_block, w_block, grid_row, grid_col)

        make_table(frame, k, addresses, longest_name, all_gelivery_items, table_title_action, button_done_action)

        i+=1

def get_max_width(n1, n2, n3):

    x = n1 if n1 > n2 + n3 else n2 + n3

    return x


"""this function makes groups of items by street name. defines the maximal height and width of each table - all the tables 
shall look the same - height and width, based on the longest name (lenght of a name column), and the group with
the most items (names)
RETURN: 
    num_blocks = the number of unique street names. How many indivitual tables will show 
    sorted_array = dictionary with key = street name; value = all the addresses(street and number) and names

"""
def make_calculations_and_possitioning(items):

    sorted_array = find_unique_addresses(items)

    max_rows = get_max_rows(sorted_array)
    max_letters = get_max_name_len(items)
    max_title = get_max_title_len(sorted_array) + 4 # 4 is for left and right space. W is wider letter

    w = get_max_width(max_title, max_letters, 3)

    width_per_block = w * WIDTH_PER_SYMBOL_PX + 20
    height_per_block = (max_rows + 1) * HEIGHT_PER_ROW_PX

    return  height_per_block, width_per_block, sorted_array, max_letters


def find_unique_addresses(items):
    one_block = dict() # key = street name; value = array of items
    num_blocks = 0
    STR_TITLE_FORMAT = "{}  ({} " + items.to_do_action + ")"
    for item in items.matrix:
        if item.street not in one_block:
            title_per_street = STR_TITLE_FORMAT.format(item.street, 1)
            one_block[item.street] = [{"name" : item.name, "address" : item.address, "title" : title_per_street}]
            num_blocks+=1
        else:
            n = len(one_block[item.street]) + 1
            title_per_street = STR_TITLE_FORMAT.format(item.street, n)
            one_block[item.street].append({"name" : item.name, "address" : item.address, "title" : title_per_street})  

    return one_block  

def sort_max_lambda(a,b):  
    return lambda a, b: a if a>=b else b  

def get_max_name_len(items):

    max_len_name = sort_max_lambda(0,0)
    y = max_len_name(0,0)
    for a in items.matrix:
        y = max_len_name(len(a.name),y)

    return y  

def get_max_rows(items):

    max_lines_func = sort_max_lambda(0,0)
    y = max_lines_func(0,0)
    for a in items.values():
        y = max_lines_func(len(a),y)

    return y  

def get_max_title_len(items):

    max_len_name = sort_max_lambda(0,0)
    y = max_len_name(0,0)
    for key in items:
        for a in items[key]:
            y = max_len_name(len(a["title"]),y)

    return y    