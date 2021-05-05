"""Pickle2Json

Converts old pickled data into the newer JSON format

Author: Josh Rogers (2021)
"""
from pbabot.main import Clock, Contact
import pickle
import jsons

try:
    with open('data.pickle', 'rb') as file:
        pickled_data = pickle.loads(file)
except FileNotFoundError:
    print('Pickled data not found.')
else:
    with open('clocks.json', 'wb') as file:
        file.write(jsons.dumpb(pickled_data['clocks']))
    with open('contacts.json', 'wb') as file:
        file.write(jsons.dumpb(pickled_data['contacts']))
    with open('memories.json', 'wb') as file:
        file.write(jsons.dumpb(pickled_data['memories']))
    with open('/dead_characters.json', 'wb') as file:
        file.write(jsons.dumpb(pickled_data['dead_characters']))
