#python variables

x = 3
y = "mehmet"
print(x)
print(y)

x = 4         # this is int (integer)
x = "ahmet"  # this is str (string)
print(x)

x = str(30) # x is '3'
y = int(30) # y is 30
z = float(30) # z is 30.0

x = 5
y = "mehmet"
print(type(x)) # int
print(type(y)) # str

a = 4
A = "ahmet"
# A and a is not the same things

# Assign Multiple Values

x, y, z = "ahmet", "mehmet", "kamil"
print(x)
print(y)
print(z)

x = y = z = "kamil"
print(x)
print(y)
print(z)

names = ["mehmet", "ahmet", "kamil"]
x, y, z = names
print(x)
print(y)
print(z)

# Output Variables

x = "Python is easy"
print(x)

x = "Python"
y = "is"
z = "easy"
print(x, y, z)

x = "Python "
y = "is "
z = "easy"
print(x + y + z) # we are adding space in `python` and `is` because we dont wanna make it like pythoniseasy

x = 5
y = 101
print(x + y)

x = 9
y = "mehmet"
print(x, y) # "we cant do + with str and int" but we can do this

# im practicing myself on global variables so i can't add it right now :(