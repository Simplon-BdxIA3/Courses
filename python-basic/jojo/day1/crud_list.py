#initialization
animals = []
#create
animals = ["dog", "cat", "turtle", "racoon"]
#read
print(animals)
print(type(animals[0]))
print(animals[2])
print(animals[-1])
print(animals[1:3])
print(animals[::2])
print(animals[1:])
print(animals[:-2])
print("************")
#update
animals[2] = "fox"
print(animals)
animals.append("elephant")
print(animals)
zoo = ["zebra", "lion"]
animals += zoo
print(animals)
animals.insert(3,"unicorn")
print(animals)
print("************")
#delete
animal = animals.pop(3)
print(animal)
print(animals)
animals.remove("zebra")
print(animals)
del animals[-1]
print(animals)