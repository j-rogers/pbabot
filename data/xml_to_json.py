"""XML2JSON

Converts old XML personal data format into the newer JSON

Author: Josh Rogers (2021)
"""
import jsons
import xml.etree.ElementTree as et

dead_characters = {}
memories = []

tree = et.parse('personal.xml')
root = tree.getroot()

# Dead characters
for rip in root.iter('rip'):
    for player in rip:
        for character in player:
            if player.tag not in dead_characters:
                dead_characters[player.tag] = {character.get('name').strip(): character.get('cause').strip()}
            else:
                dead_characters[player.tag][character.get('name').strip()] = character.get('cause').strip()

print('Dead characters:')
print(jsons.dumps(dead_characters))

for remember in root.iter('remember'):
    for group in remember.findall('group'):
        for memory in group:
            memories.append(memory.text.strip())

print('Memories:')
print(jsons.dumps(memories))
