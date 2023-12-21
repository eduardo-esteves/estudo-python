# json.dumps e json.loads com strings + typing.TypedDict
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null

import json
from pprint import pprint

from dict_types.MovieType import MovieType
from helper.print_msg_section import print_msg_section as print_msg

# CPBA 289

string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''

filme: MovieType = json.loads(string_json)

print_msg("Imprimindo o dicionário filme")
pprint(filme)

print_msg("Imprimindo um propriedade especifica do dicionário")
pprint(filme['budget'])

print_msg("Convertendo o dicionário filme para uma string JSON novamente")

json_string = json.dumps(filme, indent=4)
print(json_string)


