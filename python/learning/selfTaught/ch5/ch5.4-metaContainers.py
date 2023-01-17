#-------------------------------#
#       Meta Containers         #
#-------------------------------#

# List in a list
lists = []
rap = ["Ye", "Dr Dre", "50 Cent", "Nas"]
rock = ["The Beatles", "The Rolling Stones", "Led Zeppelin"]
blues = ["Stevie Ray Vaughan", "Buddy Guy", "Johnny Winter"]

lists.append(rap)
lists.append(rock)
lists.append(blues)

rapList = lists[0]
#print(rapList)

# After appending a new item, the change is reflected in the list as well
rapList.append("Kendrick Lamar")
#print(rapList)
#print(lists)



# Storing a tuple inside a list, a list inside a tuple,
# and a dictionary inside a list or tuple
locations = []

la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

locations.append(la)
locations.append(chicago)
#print(locations[0])

# Lists inside tuple
eights = ["Edgar Allan Poe", "Charles Dickens"]
nines = ["Hemingway", "Fitzgerald", "Orwell"]

authors = (eights, nines)
#print(authors)

# Dictionary in list and tuple
bday = {"Hemingway": "7.21.1899", "Fitzgerald": "9.24.1896"}
myList = [bday]
#print(myList)
myTuple = (bday,)
#print(myTuple)

# List, tuple, and dictionary in a dictionary
ny = {"location":
        (40.7128, 74.0059),
        
        "celebs":
        ["W. Allen", "Jay Z", "K. Bacon"],

        "facts":
        {"state":
        "NY",
        "country":
        "America"}
}
print(ny)