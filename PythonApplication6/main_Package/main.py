# File Name : Main.py
# Student Name: Shantele King 
# email: King4sl@mail.uc.edu
# Assignment Number: Assignment 10 
# Due Date: 4/10/2025
# Course #/Section: IS4010-001
# Semester/Year:Spring 2025
# Brief Description of the assignment:
# Brief Description of what this module does: Calls the class from the 
# Citations: https://pokeapi.co/
# Anything else that's relevant:


from API_Package.API import *
from DataProcessor_Package.DataProcessor import *

if __name__ == "__main__":
   
    api_client = APIClient()
    ditto_data = api_client.get_pokemon()

    Data_Processor = DataProcessor(ditto_data)
    Data_Processor.save_to_csv("ditto_data.csv")

    

    
    name = ditto_data.get("name")
    height = ditto_data.get("height")
    weight = ditto_data.get("weight")
    abilities = [ability["ability"]["name"] for ability in ditto_data.get("abilities", [])]

    print("Name:", name)
    print("Height:", height, "dm")
    print("Weight:", weight, "hg")
    print("Abilities:", ", ".join(abilities))




    import os

    print("✅ CSV exists!" if os.path.exists("data/ditto_data.csv") else "❌ CSV not found.")





