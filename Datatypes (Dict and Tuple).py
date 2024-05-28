# Dictionary (dict)

# Keys and Values
# Use the keys to get the values attached to them
# {key:value}

# Defining a dictionary object (Method 1)
car1 = {
    "brand":"Toyota", 
    "model":"Corolla",
    "year":2006
}

# Defining a dictionary object (Method 2)
car1 = dict(brand = "Toyota", model = "Corolla", year = 2006)

car2 = {
    "brand":"Honda", 
    "model":"City",
    "year":2016,
    "soldon":["Monday", "Tuesday", "Sunday"],
    1000:"Hello"
}

# Example of a nested dictionary (dict within a dict)
family = {
    "child":{
        "name":"ligma",
        "age": 10
    },
    "mother":{
        "name":"izayla",
        "age":30,
        "hobby":{
            "name":"crocheting",
            "difficulty":"really hard"
        }
    } 
}

# How to get information from a nested dictionary (multiple []s to find what you're looking for)
# Remember that python works in layers so it goes to family first ---> family["mother"] ---> family["mother"]["hobby"] and so on
diff = family["mother"]["hobby"]["difficulty"]

print(diff)

person1 = {
    "name":"jack",
    "age":10,
    "hasStolen":False,
}

# Shallow copy just means that both the objects are affected even if only of them is changed
# Deep copy means that both objects stay independant of eachother

# Deep copies one dictionary to another
person2 = person1.copy()

# Example of shallow copy
person3 = person1

# Changing key values
person1["age"] = 12
print(person2)

# Adding a key:value or changing a key value like we did above
person1.update({"father":"merlin"})
print(person1["father"])

# Removing a key from a dict
person1.pop("age")

# Removing the last added key from a dict (basically the last key in the dict)
poppedItem = person1.popitem()

# Deleting a whole dictionary
# del person1 

# Deleting all contents inside a dictionary leaving it empty {}, del deletes the variable itself as stated above
person1.clear()
print(person1)

# Getting a value from a dictionary
# Can also just do age = person1["age"]
age = person1.get("age") 
print(age)

# Gets all the keys inside a dict
print(person1.keys())

# Gets all the values inside a dict
print(person1.values())

# Gets all the keys and values inside a dict as a tuple
# (key, value), (key, value)...
print(person1.items())

# Getting a value from a dictionary
print(car1["brand"])
print(car1["year"])

# Python counts one key:value object as one item
print(len(car1))

# Tuple

# Defining a tuple (A tuple is a list that cannot be changed) (immutable)
tuple1 = (8, 1, 10, "Hello", True)

# Some functions from lists work on tuples as long as they aren't meant to change the list (won't work on tuples) e.g. append, pop
print(tuple1[0:3])
print(tuple1.index(1))
print(tuple1.count(10))

print(tuple1)

# Defining a set
# A set is always ordered and cannot contain duplicate items
set1 = {1, 2, 4}
set2 = {1, 10, 4, 11, 5, 2}

print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.union(set2))

# Gets elements that are unique to both sets and are not present in both of them
print(set1.symmetric_difference(set2))

print(set1.issubset(set2))
print(set2.issuperset(set1))

