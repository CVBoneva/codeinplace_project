import random

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

        my_names_array = FIRST_NAME
        my_family_names_array = LAST_NAME
        my_street_names = STREET_NAME

        my_array = []
        how_many = random.randint(5,20)
        for _ in range(how_many):
            my_name = random.choice(my_names_array) + " " + random.choice(my_names_array) + " " + random.choice(my_family_names_array)
            my_street = random.choice(my_street_names)
            my_number = random.randint(1,50)
            my_item = DeliveryItem(my_name, my_street, my_number)
            my_array.append(my_item)

        self.matrix = my_array

class DeliveryItem():

    def __init__(self, name, street, number):
        self.name = name
         
        self.street = street + " str."
        self.number = number 
        self.address = self.street + " " + str(self.number)