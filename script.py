import random

# global variables
my_name = "Luis Ospina"
fName = "Luis "
lName = "Ospina"
fullName = fName + lName
print("Hello and welcome " + my_name + '!')
print(type(my_name))
print(fullName)

one = 1
two = float(2)
print(one)
print(two)

social_media = ["instagram", "snapchat", "facebook", "tiktok"] # this is a list
i, s, f, t = social_media
print(i)
print(t)

def myfunc():
    # if you want to change the global variable above, first type global and then the variable,
    # in a new line, set the variable to new value
    global Os 
    Os = "Windows"
    language = "Python" #local variable
    print(my_name + ", I am learning " + language)

myfunc()
print(Os)

print(random.randrange(1,10))

multi_line_string = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(multi_line_string)
print(multi_line_string[4])
print(len(multi_line_string))
if "elit" in multi_line_string:
    print("Yes, 'elit' is in multi_line_string")
if "english" not in multi_line_string:
    print("No, 'english' is not in multi_line_string")

for x in fName:
    print(x)

#position 2 is included, 7 is not included
# slicing
hello_world = "Hello World!"
print(hello_world[2:7])
print(hello_world[:5]) #get first 5 characters
print(hello_world[6:]) #get from index 6 to end
print(hello_world[-6:-1]) #includes -6 not -1
print(hello_world.upper())
print(hello_world.lower())
print(hello_world.strip()) # removes white space from beginning and end of string
print(hello_world.replace("l", "L"))

hello_world_plus_number = "Hello world! Here is a number {}. Here is another number {}."
print(hello_world_plus_number.format(one, two))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))