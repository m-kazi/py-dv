# importing pi from math
from math import pi


# importing random and creating as an Alias
import random as rdm

print(rdm.choice("123"))

# to know what to use from a module
# for item in dir(rdm):
#     print(item)


# importing local file modules_city
import modules_city

print(modules_city.capital)
modules_city.randomfunfact()

# one value every module has __name__
print(__name__)
print(modules_city.__name__)
