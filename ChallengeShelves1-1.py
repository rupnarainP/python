import shelve
#
# books = shelve.open('book')
# books['recipes'] = {'blt': ['bacon', 'lettuce', 'tomato', 'bread'],
#                      'beans_on_toast': ['beans', 'bread'],
#                      'scrambled_eggs': ['eggs', 'butter', 'milk'],
#                      'soup': ['tin of soup'],
#                      'pasta': ['pasta', 'cheese']}
#
# books['maintenance'] = {'stuck': ['oil'],
#                          'loose': ['gaffer tape']}
#
# print(books['recipes'])
# print(books['maintenance'])
#
# books.close()

locations = shelve.open('locations')
locations["0"] = {"desc": "You are sitting in front of a computer learning Python", "exits": {}}
locations["1"] = {"desc": "You are standing at the end of a road before a small brick building", "exits": {"W": "2", "E": "3", "N": "5", "S": "4", "Q": "0"}},
locations["2"] = {"desc": "You are at the top of a hill", "exits": {"N": "5", "Q": "0"}}
locations["3"] = {"desc": "you are inside a building, a well house for a small stream", "exits": {"W": "1", "Q": "0"}}
locations["4"] = {"desc": "You are in a valley besides a stream", "exits": {"N": "1", "W": "2", "Q": "0"}}
locations["5"] = {"desc": "You are in the forest", "exits": {"W": "2", "S": "1", "Q": "0"}}
locations.close()

keyWords = shelve.open('vocabulary')
keyWords["NORTH"] = "N"
keyWords["EAST"] = "E"
keyWords["SOUTH"] = "S"
keyWords["WEST"] = "W"
keyWords["QUIT"] = "Q"
keyWords.close()

