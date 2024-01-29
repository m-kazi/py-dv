##Lists are one of the four collection data types

users = ['Dave', 'John', 'Sara']
print(users)

mylist = list([1, 'Yo'])
print(mylist)

data = ['Kazi', 30, True]

emptylist = []

#To check if the data is there or not
# print('John' in users) #True
# print('John' in data) #False

# print(users[0])
# print(users[-1])

# print(users[0:2])
# print(users[1:])
# print(users[-3:-1])

# print(users.index('Sara'))

# print(len(data))

users.append('Kazzcode')
print(users)

#To add into the previously existing users list
users += ['Jason']
print(users)

users.extend(['Robin', 'Batman'])
print(users)

#Adding a list into another list
# users.extend(data)
# print(users)

#Adding into a position
users.insert(0, 'Bob')
print(users)

#To add
users[2:2] = ['Eddie', 'Alex']
print(users)

#To replace
users[1:3] = ['Rob', 'JPJ']
print(users)


#Remove methods from list

users.remove('Bob')
print(users)

#Removes & Returns the last value
print(users.pop())
print(users)

#To delete a specific value
del users[0]
print(users)

#To delete the list itself
# del data

#To delete the data from the list & make it empty
print(data)
data.clear()
print(data)

#To sort alphabatically
users.sort()
print(users)

#Lower case always comes last after the uppercase
users[1:2] = ['ben']
users.sort()
print(users)

#So that it sorts whether it's a lower or upper case
users.sort(key=str.lower)
print(users)

#Numbers sorting
nums = [5, 10, 20, 50, 30]
# nums.reverse()
print(nums)

#Ascending & Descending 
# nums.sort()
# nums.sort(reverse=True)
# print(nums)

#Sorting without modifying the original list
print(sorted(nums, reverse=True))
print(nums)

#To copy lists & create a new one
newcopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(newcopy)
print(mynums)
print(mycopy)
print(type(nums))