## Tuples are like lists except the data inside tuples will not change. 
#the order of the data will not change

mytuple = tuple(('Kazi', 30, True))
anothertuple = (3, 3, 50, 6, 7)

print(mytuple)
print(anothertuple)
print(type(mytuple))
print(type(anothertuple))

#To create a new tuple and modify, create a new list then modify and convert into tuple 
newlist = list(mytuple)
newlist.append('Kazzcode')
newtuple = tuple(newlist)
print(newtuple) 

#Unpacking and save the data into variable
(one, two, *yo) = anothertuple
print(one)
print(two)
print(yo)

print(anothertuple.count(3))