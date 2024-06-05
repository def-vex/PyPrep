# Augmented Operators

# Syntax: val1 <operator>= val2 ---> val1 = val1 <operator> val2
int1 = 10
int2 = 3

int1 //= int2
int1 **= 2
int2 *= 10

# Datatype Coversion

# String to Boolean
# Python takes empty strings as False and the opposite as True
# This means that "True" is True and so is "False" while "" is False (space characters also count as non empty)
stringVal = " "
print(bool(stringVal))

# Integer to Boolean
# Returns True for every value except 0 (for which it returns False instead)
boolVal = bool(-1)
print(boolVal)

# Converting the inputted datatype straight away (place datatype keyword on the input function)
x = int(input("Input an integer: "))
print(x)

floatVal = float(x)
print(floatVal)

# Converts float back to integer and rounds down
x = int(floatVal)
print(x)

# Mess around with more datatype conversions!
# Get datatype of a variable by type(<name>)
x = int(input())
y = 200 
datatype = type(x)

print(datatype)

x = str(x)
datatype = type(x)

print(datatype)

list1 = [1, 10, 23]
print(type(list1))

tuple1 = tuple(list1)
print(tuple1)
print(type(tuple1))