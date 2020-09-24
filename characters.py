import json
from PIL import Image
import requests
from io import BytesIO

with open('marvel_characters.json') as f:
	data = json.load(f)

character_database = {}

for item in data['marveldict']:
	for index, character in enumerate(item['data']['results']):
		name = character['name']
		description = character['description']
		thumbnail = character['thumbnail']['path'] + '.' + character['thumbnail']['extension']
		character_database[name] = [description,thumbnail]



while(True):
	superhero = input("Enter Name of your favourite Marvel Character: ")
	if superhero == "quit": break
	try:

		if character_database[superhero][0]:
			print(character_database[superhero][0])
		else:
			print("Sorry, a description is not available for this character")
		im = requests.get(character_database[superhero][1])
		if im:
			img = Image.open(BytesIO(im.content))
			img.show()
		else:
			print("No image available")

	except:
		print("No such character is present")