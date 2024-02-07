# for command line arguments


def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "Bangla": "Ki Obostha",
    }
    msg = f"{greetings[lang]} {name}!"
    print(msg)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog="GreetingProgram", description=" Personal Greeting"
    )

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="Name of the person to greet.",
    )

    parser.add_argument(
        "-l",
        "--lang",
        metavar="language",
        required=True,
        choices=["English", "Spanish", "Bangla"],
        help="The language of the greeting.",
    )

    args = parser.parse_args()

    hello(args.name, args.lang)
