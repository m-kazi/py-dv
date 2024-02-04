name = "Tanim"
count = 2


# can get access to the Global "count"
def parent():
    color = "blue"
    global count
    count += 1
    print(count)

    # can reassign "color" value in local scope
    def child(greeting):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    child("welcome")


parent()
