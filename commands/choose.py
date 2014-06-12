import random

from JakeBot import Command


@Command(name="choose", help="Choose a random item out of the provided choices.")
def choose(chat, message, args, sender):
    if len(args) == 0:
        chat.SendMessage("Specify at least one option.")
        return
    rand = random.randint(0, len(args) - 1)
    choice = args[rand]
    chat.SendMessage("I choose...{0}".format(choice))