import random
import json

FIRST_NAME = ["Olivia", "Amelia", "Isla", "Lily", "Ava", "Freya", "Ivy", "Sophia", "Grace", 
                          "Willow", "Mia", "Isabella", "Daisy", "Elsie", "Evie", "Florence", "Ella", 
                          "Emily", "Evelyn", "Luna"]
LAST_NAME = ["Bailey", "Baker", "Carver", "Charlton", "Dacre", "Elwood", "Jarvis", "Kendall", "Lester", "Percy"]
STREET_NAME = ["Lotus", "Jasmine", "Marigold", "Rose", "Sunflower", "Hibiscus", "Orchid", "Gladiolus"]

"""
Generates delivery items - set of address and name. From predefined arrays randomly generated combinations. 
Can be replaced with different sources as text file, db sql
"""

class DeliveryItems():

    matrix = []
    title = "my final project in Code in Place"

    def SortFunction(self, e):
        return e.street
    
    def __init__(self, file_name):

        
        self.matrix = self.load_data(file_name)

    def test_to_json(self):
        
        make_json = self.toJSON()
        f = open("items.json", "w")
        f.write(make_json)
        f.close()    

    def load_data(self, file_name):

        try:
            data_array = self.read_from_file(file_name) 
            print("data read from file")
        except Exception as e: 
            print(e)
            data_array = self.load_from_arrays()  
            self.title = "My Delivery List" 
            print("data read from arrays")

        return data_array     

    def  load_from_arrays(self):

        my_names_array = FIRST_NAME
        my_family_names_array = LAST_NAME
        my_street_names = STREET_NAME

        my_array = []
        how_many = random.randint(5,20)
        for _ in range(how_many):
            my_name = random.choice(my_names_array) + " " + random.choice(my_names_array) + " " + random.choice(my_family_names_array)
            my_street = random.choice(my_street_names) + " str."
            my_number = random.randint(1,50)
            my_item = DeliveryItem(my_name, my_street, my_number)
            my_array.append(my_item)

        return my_array
    
    def  read_from_file(self, file_name):
         
        file_name = "items.json" if len(file_name) == 0 else file_name
        f_handler = open(file_name)
        json_txt = f_handler.read()
        item_objects = json.loads(json_txt)
        f_handler.close() 

        print(item_objects)

        my_array = self.toObject(item_objects)

        return my_array

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4)   

    def toObject(self, to_deserialize):
        my_array = []
        self.title = to_deserialize["title"]
        items = to_deserialize["matrix"]
        for item in items:
            my_name = item["name"]
            my_street = item["street"]
            my_number = item["number"]
            my_item = DeliveryItem(my_name, my_street, my_number)
            my_array.append(my_item)

        return my_array    


class DeliveryItem():

    def __init__(self, name, street, number):
        self.name = name
         
        self.street = street 
        self.number = number 
        self.address = self.street + " " + str(self.number)