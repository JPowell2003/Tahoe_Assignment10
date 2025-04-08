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

if __name__ == "__main__":
   
    api_client = APIClient()
    ditto_data = api_client.get_pokemon()  
    
    name = ditto_data.get("name")
    height = ditto_data.get("height")
    weight = ditto_data.get("weight")
    abilities = [ability["ability"]["name"] for ability in ditto_data.get("abilities", [])]

    print(f"Name: {name}")
    print(f"Height: {height} dm")
    print(f"Weight: {weight} hg")
    print(f"Abilities: {', '.join(abilities)}")

