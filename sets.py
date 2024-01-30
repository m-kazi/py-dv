# Sets

set1 = {1, 2, 3, 4}
set2 = set((10, 20, 30, 40))

print(set1)
print(set2)
print(type(set1))
print(len(set1))


# no duplicates allowed
nums = {1, 2, 2, 3}
print(nums)

# 1 is duplicate of True, 0 is dupe of False
nums = {1, True, 2, 3, False, 0, 7}
print(nums)

# check if a value is in set
print(3 in nums)

# add a new element to set
nums.add(8)
print(nums)

# Add elements from one set to another set
set1.update(set2)
print(set1)
print(set2)


# mere two sets to create a new set
one = {1, 2, 3}
two = {4, 5, 6}

mynewset = one.union(two)
print(mynewset)
print(one)
print(two)

# keep only duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.intersection_update(two)
print(one)
print(two)

# keep everythin except duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)
print(two)
