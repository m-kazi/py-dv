def hello():
    print("Hello world!")


hello()


# with parameter
def sum(num1=0, num2=0):
    if type(num1) is not int or type(num2) is not int:
        return
    return num1 + num2


total = sum()
print(total)


# not sure how many parameters we will pass
def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("kazi", "tanim")


# With keyword arguments
def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(first="John", last="Cena")
