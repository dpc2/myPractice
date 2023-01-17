# 1.4.1.e - Dicts

capitals = {"California": "Sacramento", "Colorado": "Denver"}
print(capitals)
print(capitals['Colorado'])
capitals['Washington'] = 'Seattle'
print(capitals)
capitals['Oregon'] = 'Portland'
print(len(capitals))
print('\n')

for i in capitals:
    print(capitals[i], "is the capital of", i)
print('\n')

# Methods for Dictionaries

phoneExt = {"Tweedle Dee": 1862, "Tweedle Dum": 1865}
print(phoneExt)
print(phoneExt.keys())
list1 = list(phoneExt.keys())
print(list1)
print("Tweedle Dee" in phoneExt)
# 1865 is not a key
print(1865 in phoneExt)
print(phoneExt.values())
list2 = list(phoneExt.values())
print(list2)
print(phoneExt.items())
list3 = list(phoneExt.items())
print(list3)
print(phoneExt.get("Tweedle Dum"))
print(phoneExt.get("Tweedle Dum", "NO ENTRY"))
del phoneExt["Tweedle Dee"]
print(phoneExt)
print('\n')
