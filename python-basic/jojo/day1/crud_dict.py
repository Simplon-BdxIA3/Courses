#initialization
thisdict = {}
#create
thisdict = {
    "brand": 'Ford',
    "model": 'Mustang',
    "color": 'dirty pink',
    "years": [1964, 1956],
    2: 'deux'
}
print(thisdict)
#read (pour retrouver un element on utilise les keys)
print(list(thisdict.keys()))
print(list(thisdict.values()))
print(thisdict["years"])
print(thisdict["years"][0])
print("************")
#update
thisdict["color"] = 'dirty blond'
print(thisdict)
thisdict["max speed"] = 'OMG'
print(thisdict)
print("************")

#delete
del thisdict[2]
print(thisdict)
thisdict.pop("max speed")
print(thisdict)