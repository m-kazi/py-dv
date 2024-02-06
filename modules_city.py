from random import choice

capital = "Dhaka"
bird = "Doyel"
flower = "Shapla"


def randomfunfact():
    funfacts = [
        "Dhaka is a beautiful city.",
        "Dhaka has too much traffic & population.",
        "One of the crowded places in the world.",
    ]

    index = choice("012")

    print(funfacts[int(index)])


# only runs if this matches
if __name__ == "__main__":
    randomfunfact()
