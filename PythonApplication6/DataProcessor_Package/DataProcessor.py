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
import requests
import os

class DataProcessor:
    def __init__(self):
        self.url = "https://pokeapi.co/api/v2/pokemon/ditto"
        self.data = {}

    def load_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.data = response.json()

    def flatten(self, data, parent_key='', sep='_'):
        flat = {}
        if isinstance(data, dict):
            for key in data:
                new_key = f"{parent_key}{sep}{key}" if parent_key else key
                flat.update(self.flatten(data[key], new_key, sep))
        elif isinstance(data, list):
            for i, item in enumerate(data):
                new_key = f"{parent_key}{sep}{i}"
                flat.update(self.flatten(item, new_key, sep))
        else:
            flat[parent_key] = data
        return flat

    def save_to_csv(self, filename):
        flat_data = self.flatten(self.data)

        path = os.path.join(os.path.dirname(__file__), filename)

        with open(path, "w", newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=flat_data.keys())
            writer.writeheader()
            writer.writerow(flat_data)