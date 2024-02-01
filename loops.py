## while loop
value = 1

# while value <= 10:
#     value += 1
#     if value == 5:
#         break
#     print(value)

##continue stops to the current iteration & goes to the next one
# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is : " + str(value))

##For loop
names = ["Kazi", "Tanim", "Sara", "James"]

# for x in names:
#     print(x)

# for x in names:
#     if x == "Sara":
#         break
#     print(x)

# for x in names:
#     if x == "Sara":
#         continue
#     print(x)

# looping through a range of numbers
# for x in range(5):
#     print(x)

# range(start, finish)
# for x in range(1, 5):
#     print(x)


# range(start, finish, increment by 5)
# for x in range(0, 51, 5):
#     print(x)
# else:
#     print("Glad that's over!")

# looping through nested lists
names = ["Kazi", "Tanim", "Sara", "James"]
actions = ["codes", "eats", "sleeps"]

# here name is the outer loop
# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")
