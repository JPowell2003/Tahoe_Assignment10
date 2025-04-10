# File Name : DataProcessor.py
# Student Name: Justin Ganduri
# email: gandurpn@mail.uc.edu
# Assignment Number: Assignment 10 
# Due Date: 4/10/2025
# Course #/Section:  IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment:
    # The assignment gets data about the Pokémon Ditto from an API, processes it into a CSV file, and displays some of its basic information
# Brief Description of what this module does:
    #Flattens nested Pokémon data into a flat dictionary format and saves it as a CSV file
# Citations: https://pokeapi.co/
# Anything else that's relevant:

import csv

class DataProcessor:
    '''
    Processes and flattens nested JSON data, and saves it to a CSV file.
    '''

    def __init__(self, data):
        '''
        Initialize the DataProcessor with JSON data
        @param data: A nested dictionary (e.g., API response for a Pokémon)
        '''
        self.data = data

    def flatten(self, data, parent_key='', sep='_'):
        '''
        Flatten nested dictionaries and lists into a single dictionary
        @param data: The data to flatten (dict or list)
        @param parent_key: Internal key used for recursion (do not modify)
        @param sep: Separator used between nested keys (default is "_")
        @return: A flat dictionary with compound keys
        '''
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
        '''
        Save the flattened data to a CSV file in the 'Data/' directory
        @param filename: The name of the file to save (e.g., "ditto_data.csv")
        @return: None, prints a success or failure message
        '''
        flat_data = self.flatten(self.data)
        full_path = "Data/" + filename  # Assumes "Data/" already exists

        try:
            with open(full_path, "w", newline='', encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=flat_data.keys())
                writer.writeheader()
                writer.writerow(flat_data)
            print("File saved successfully to '" + full_path + "'")
        except Exception as e:
            print("Failed to save file to '" + full_path + "': " + str(e))
