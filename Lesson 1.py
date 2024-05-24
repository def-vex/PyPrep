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
list1 = [1, 2, 3, "Hello", 5, 6, True, 8, 4.103, 10]

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


