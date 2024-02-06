person = "Tanim"
coin = 3

print("\n" + person + " has " + str(coin) + " coins left.")

# older way of string
# first %s represent 'person', second %s represent 'coin'
message = "\n%s has %s coins left." % (person, coin)
print(message)


# newer way of string using .format() method.
# first {} represent 'person', second {} represent 'coin'
message = "\n{} has {} coins left.".format(person, coin)
print(message)

# using index numbers starting with 0
message = "\n{1} has {0} coins left.".format(coin, person)
print(message)

# using specific values and can be changed
message = "\n{person} has {coin} coins left.".format(coin=coin, person="Dave")
print(message)

# using dictionary to pass the value
human = {"person": "Kazi", "coin": "5"}

message = "\n{person} has {coin} coins left.".format(**human)
print(message)

################### Startng f-String ######################
####### This is the way !

# regular way
message = f"\n{person} has {coin} coins left."
print(message)

# specific value way
message = f"\n{person} has {5 * 2} coins left."
print(message)

# using method inside it {}
message = f"\n{person.lower()} has {coin} coins left."
print(message)

# using lists to pass the value
message = f"\n{human['person']} has {coin} coins left."
print(message)

########### You can pass format options

# example of 2 values after decimal 'num:.2f' - here 2f is fixed by 2 nums
num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

# looping through a range
for num in range(1, 6):
    print(f"2.25 times {num} is {2.25 * num:.2f}\n")

# looping through a range for % percentage
for num in range(1, 6):
    print(f"{num} is divided by 4.52 {4.52 * num:.2%}")
