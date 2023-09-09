# Challenge #1: List of favorite musicians
favMusicians = ["Allman Brothers Band", "Bob Dylan", "Stevie Wonder"]


# Challenge #2: List of tuples, latitudes and longitudes
sanDiego = (32.7730, -117.2516)
bayArea = (37.6614, -122.4673)
englewood = (39.6557, -104.9650)
myLocations = [sanDiego, bayArea, englewood]
#print(myLocations)


# Challenge #3: Dictionary with personal attributes
self = {
    "height": "6'2\"",
    "hair color": "brown",
    "eye color": "blue",
    "favorite author": "Tolkien"
}
#print(self)


# Challenge #4: Get to know me
def askAway():
    question = input("Ask a question!\n")
    if question in self:
        print(self[question])
    else:
        print("Ask something else!")

#askAway()


# Challenge #5: Dictionary with song lists
songs1 = ["Blue Sky", "Mountain Jam", "One Way Out"]
songs2 = ["Blowin' in the Wind", "The Man in Me", "Baby Let Me Follow You Down"]
songs3 = ["Ordinary Pain", "Misstra Know It All", "As"]

musiciansDict = {
    favMusicians[0]: songs1,
    favMusicians[1]: songs2,
    favMusicians[2]: songs3
}

#print(musiciansDict)


# Challenge #6: Python sets - unordered, non-iterable, immutable, no duplicates
mySet = {"apple", "banana", "cherry"}
print(mySet)