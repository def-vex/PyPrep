# Assigning multiple variables in one line

x = 10
y = 11
z = 12

x, y, z = 10, 11, 12

# Unpacking a list/tuple
# Make sure the list has the same number of elements as the variables it's being unpacked to
fruits = ["Banana", "berry", "mango"]
f1, f2, f3 = fruits

# Swapping variables
x, y = y, x

# Escape Sequences

# \n = New Line
print("The fruit's name:", f1, 10, f2, sep=" ", end="\n")

# \" = "
# \' = '
# \\ = \
print("\\")

# \t = Horizontal Tab
print("The weather is \t good")

# \0 = Null Value
print("\0")

# \b = Backspace
# Moves the python printing cursor back one space (character doesn't get removed UNLESS it's overwritten)
print("12345\b\b\b", end="")

# After 3 \b, the cursor is now at 3 so anything being printed on the same line will now overwrite the previously written "345"
print("BRO")



