# File Name : API.py
# Student Name: Jay Powell
# email: powela9@mail.uc.edu
# Assignment Number: Assignment 10 
# Due Date: 4/10/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:
# Brief Description of what this module does:
    #Connects to the PokeAPI to retrieve data about the Pokemon Ditto.
# Citations: https://pokeapi.co/
# Anything else that's relevant:

import requests
import json

class APIClient:
    '''
    Connects to the PokeAPI and retrieves information about a specific Pokemon.
    '''
    def __init__(self):
        '''
        Initializes the APIClient with a URL pointing to the Ditto Pokemon
        '''
        self.url = "https://pokeapi.co/api/v2/pokemon/ditto"

    def get_pokemon(self):
        '''
        Sends a get request to the PokeAPI and retrieves the data for Ditto.
        @return: A dictionary containing data about the Pokemon Ditto.
        '''
        response = requests.get(self.url)
        data = json.loads(response.content)
        return data

