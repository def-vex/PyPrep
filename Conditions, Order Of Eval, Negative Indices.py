# Conditions

# Syntax if <condition(s)>: (don't forget the colon)
# elif = else if <conditon(s)>
# end with else: (You don't HAVE to end your if statements with else as shown on lines 25-26)

x = 10
y = 30

if x == y:
    print("X is equal to Y")
elif x > y:
    print("X is greater than Y")
else:
    print("Y is greater than X")

licenseExpired = False
inTrouble = False
stolenCar = False
goodPerson = False

under18 = True

# If you want to perform a check always then perform other checks you can always split your if statements so Python goes through all of them atleast once
if under18:
    print("Arrest")

# Make sure your top priority if statements are at the top
# Join different conditions with relational operators (and not or)
if licenseExpired and stolenCar and inTrouble:
    print("Execution")
elif licenseExpired and inTrouble and not stolenCar:
    print("Arrest")
elif licenseExpired:
    print("Ticket")
elif inTrouble and goodPerson:
    print("Let them go")
else:
    print("Annoy them by making them wait 10 minutes")

# Order of Evaluations

# 1) Mathematical (+ - ** / etc.)
# 2) Relational (== != > < etc.)
# 3) Logical (and not or)

# Python goes from left to right when same precedence
total = 3 - 10 + 10

res = 7 + 10**2 / 2 * 10 - 3 == 504.0 and False

# Negative Indices
# Access elements from the end of your list efficiently
# Works both on lists and strings (like normal positive indices work on both)

list1 = [1, 2, 4, 10]

list1.append(11)
list1.append(12)
list1.append(13)
list1.append(20)
list1.append(21)

print(list1)

# This works too
print(list1[len(list1)-1])

# But this is faster and more efficient because you're not calling the len function and telling Python to count all the elements again and again
print(list1[-1])

str1 = "Hello World"
print(str1[-4])

# Make sure your step is negative too if you're splicing!
print(list1[-1:-3:-1])
