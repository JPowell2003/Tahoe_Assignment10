# File Name : DataProcessor.py
# Student Name: Justin Ganduri
# email: gandurpn@mail.uc.edu
# Assignment Number: Assignment 10 
# Due Date: 4/10/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:
# Brief Description of what this module does:
    #Connects to the PokeAPI to retrieve data about the Pokemon Ditto.
# Citations: https://pokeapi.co/
# Anything else that's relevant:

import csv

class DataProcessor:
    """
    This class processes Pokemon data and saves it into a CSV file.
    """

    def __init__(self, data):
        """
        Stores the Pokemon data received from the API.
        """
        self.data = data

    def save_to_csv(self, filename):
        """
        Extracts name, height, weight, and base_experience from the data
        and writes them into a CSV file.
        """

        name = self.data["name"]
        height = self.data["height"]
        weight = self.data["weight"]
        base_experience = self.data["base_experience"]

       
        with open("Data/" + filename, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Height", "Weight", "Base Experience"])  
            writer.writerow([name, height, weight, base_experience])        

        print("Data saved to", filename)

