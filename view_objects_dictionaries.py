# this is newer version 
# view objects allow you to peak in to view keys and values and all the items

players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}
# print(players.keys())  this prints dict_keys and the the keys wrapper in parens (this means there is an object or in this case dictionary view object)
# print(players.values())
# print(players.values()[0]) cannot treat view objects like a list-this returns an error*********
# print(players.items())
# everytime we run a query it runs on a thread***


# print(list(players.values())[1]) #cannot view object like a list-cast it as a list here to return the list value

#to copy the list-for thread safe programming
# player_names = list(players.copy().values()) - using the copy function correa Altuve Bregan Gattis Springer, accessed only by us 

