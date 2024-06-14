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
    
    def __init__(self):

        
        self.matrix = self.load_data()

    def test_to_json(self):
        
        make_json = self.toJSON()
        f = open("items.json", "w")
        f.write(make_json)
        f.close()    

    def load_data(self):

        try:
            data_array = self.read_from_file() 
        except Exception as e: 
            print(e)
            data_array = self.load_from_arrays()   

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
    
    def  read_from_file(self):
         
        f_handler = open("items.json")
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