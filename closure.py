# Closure is a funcion having access to the scope of it's parent function
# even after the parent function has returned

# good practice to avoid creating global variable while child function can acceess parent function scope

# here play_game() still has access to the parent function scope after return

# same applies for the function parameters as the variables


def parent_function(person, coin):
    # coin = 3

    def play_game():
        nonlocal coin
        coin -= 1

        if coin > 1:
            print("\n" + person + " has " + str(coin) + " coins left.")
        elif coin == 1:
            print("\n" + person + " has " + str(coin) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")

    return play_game


# john & danny is a funtion coz of returning the function
john = parent_function("John", 3)
danny = parent_function("Danny", 5)

john()
john()
john()

danny()
danny()
