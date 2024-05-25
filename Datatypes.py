# All datatypes in Python (excluding a few advanced ones)

int # Integer
str # String
float # Float (Decimal)
bool # Boolean
list # Lists/Arrays
set # Sets
tuple # Tuples (Immutable Lists)
dict # Dictionary
complex # Complex Numbers

# Integer / Float

# Defining variables (use single = sign)
int1 = 21
int2 = 3

print(int1 + int2) # Addition
print(int1 - int2) # Subtraction
print(int1 * int2) # Multiplication
print(int1 // int2) # Gives a rounded down whole number
print(int1 / int2) # Division
print(int1 ** 0.5) # Exponent/Power
print(int1 % int2) # Remainder

float1 = 1.23
float2 = 406.9406

# String

str1 = "Hello" 
str2 = "World"

# Concatenate the strings (combine)
str3 = str1 + str2
str4 = "Hello" + "World"
str5 = "Hello""World"
str6 = str1 + " " + str2 + "!"

# Multiply strings
str7 = str1*3

# Check for string length (How many characters in string)
print(len(str1))
print(len("Hello World!"))

# Show character at some position in the string (Python counts from 0) (Same as in lists)
# Syntax: stringname[index] where index can also just be an integer variable or a constant value like 4 down below
print(str1[4])

# Boolean

bool1 = True 
bool2 = False

# Reserved keywords can't be used as variable names
# E.g. you can't do True = 10

True # bool
"True" # str

# Logic operations
# Check and not or logic gates
# Can also use 1 as True and 0 as False

# Use double = sign to compare values (if equal to or not)
1 and 1 == 1

print(True == (not False))

False or False == False
not True == False

True and False == False

# Is NOT equal to (Again, to compare values)
10 != 12

print("Hello" != "World")

# List

# Arrays are lists which only have 1 type of datatype, no such thing as arrays in Python but you can technically have one if your LIST has only 1 datatype
list1 = [1, 2, 3, "Hello", 5, 6, True, 8, 4.103, 10, 2]

# To check for a list/string size/length
print(len(list1))

# To show a list's/string's element, we use it's index value
# Syntax: listname[index]
# Counting indexes starts from 0
print(list1[3])

# Use an integer variable inside
index = 4
print(list1[index])

# Can use on strings too
print(str1[0])

# List/string splicing
# Syntax: listname[start:stop] and it ignores the stop index
partOfList = list1[1:4]
print(partOfList)

# Steps inside splicing
# Syntax: listname[start:stop:step] and it ignores the stop index
partOfList = list1[0:9:2]
print(partOfList)

# Leaving an empty space after the colon sets the stop to max index
partOflist1 = list1[3:]

# Doing the same before the colon sets the start to 0 (default value)
partOflist1 = list1[:8]

# If you leave the step empty too (e.g. list1[::]), the default step value will be 1
partOflist1 = list1[::2]

# Getting a list in reverse, set your step to a negative value 
partOflist1 = list1[8:0:-1]
print(partOflist1)

# Can use these ^ on strings as well

# Attaches the value at the end of the list
# Syntax: listname.append(object)
list1.append(11)
list1.append(3)
print(list1)

# Clears the list 
list1.clear()

# Extend's argument has to be a list
list1.extend([3, 10, 11, 32, 10, 100, 100, 100, 34, 21, 110, 2000])

# Append will treat the list inside as a separate element
# list1.append([14, 20, 2])
print("----------------")
print(list1)
print(len(list1))

# Index returns the index of the value taken as input
# Syntax: listname.index(value)
print("10 is at index:", list1.index(10))

# Specify start and stop to search the rest of the array
# Syntax: listname.index(value, start, stop)
print("10 is at index:", list1.index(10, 2, 6))

# Pop extracts a value from the list at the given index
# Syntax: listname.pop(index)
value = list1.pop(4)
print("Popped value is:", value)
print(list1)

# Remove removes an object from the list and it takes in the value of the object (incase you don't know the index and don't want the removed value)
# Syntax: listname.remove(value)
list1.remove(11)
print(list1)

# Sorts the array in ascending order by default
list1.sort()
print(list1)

# Takes in a reverse argument that just gives you list in descending order
list1.sort(reverse=True)

# Inserts an object at a given index
# Syntax: listname.insert(index, object)
list1.insert(3, "Hello")
print("List 1:", list1)

# Copies the list into the list being defined
# If we use list2 = list1 instead, whatever you do to list2, happens to list2 and vice versa (they become dependant on eachother)
list2 = list1.copy()

list1.append("World")
print("List 1:", list1)
print("List 2:", list2)

# Counts the number of times a value has shown up inside a list
count = list1.count(100)
print("shows up:", count, "times")

# Also works on strings
str8 = "Raahim Mujtaba Zaid Azzaam Zaid"
print(str8.count("Zaid"))

# Reverses the list
list1.reverse()
print(list1)