#string data type

#literal assignment
first = "Kazi"
last = "Tanim"

#to check the data type
# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

#constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))


#Concatenation
fullname = first + " " + last
# print(fullname)

fullname += "!"
# print(fullname)

#Casting a number to string
decade = str(2024)
# print(type(decade))
# print(decade)

statement = "I like rock music from " + decade + "s."
# print(statement)

#Multiple lines
multiline = '''
Hey, you?

wassup !

            All good ?
'''
# print(multiline)


#Escaping special characters
sentence = 'I\'m back,\t wassup\n Let\'s code\\& fun.'
# print(sentence)

#String methods
print(first)
print(first.lower())
print(first.upper())

print(multiline.title())
print(multiline.replace("you", "me"))

print(len(multiline))
multiline += "              "
multiline = "         " + multiline
print(len(multiline))

print(len(multiline.strip()))   #to remove the white space
print(len(multiline.lstrip()))  #to remove the white space from the Left
print(len(multiline.rstrip()))  #to remove the white space from the Right

print("")
print("")

#Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$3".rjust(4))

print("")
print("")

#String index values
print(first[0])
print(first[-1])
print(first[1:3])
print(first[1:])


#Some methods return boolean value
# print(first.startswith("K"))
# print(first.endswith("I"))

# Boolean data type
myValue = True
x = bool(False)
print(type(x))
print(isinstance(myValue, bool))

# Numeric data types

#integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

#float type
gpa = 3.35
y = float(2.25)
print(type(gpa))

#complex type || data science
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers

print(abs(gpa)) #for absolute value
print(gpa * -1) #for negative value
print(abs(gpa * -1)) #will give the absolute value
print(round(gpa)) #to rounded down
print(round(gpa, 1)) #to rounded up

#module
import math
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#Casting a string to a number
zip = "20147"
zip_val = int(zip)
print(type(zip_val))

