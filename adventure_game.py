import time
import random

planets = ["Tatooine", "Endoor", "Dagobah"]
planet = random.choice(planets)
if planet == "Tatooine":
    villain = "Tusken Raiders"
elif planet == "Endoor":
    villain = "Stormtrooper"
elif planet == "Dagobah":
    villain = "Darth Vader"


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    if planet == "Tatooine":
        print_pause("You find yourself standing in the middle of the hot "
                    "desert, surrounded by sand and a few womp rats.")
        print_pause("Rumor has it that a gang of sand people is somewhere "
                    "around here, and has been terrifying the nearby town.")
        print_pause("In front of you is a hut.")
        print_pause("To your right is a crashed speedster.")
        print_pause("In your hand you hold your trusty "
                    "(but not very effective) blasters.")
    elif planet == "Endoor":
        print_pause("You find yourself standing in the middle the woods, "
                    "surrounded by trees and a few ewoks.")
        print_pause("Rumor has it that the last squadron of stormtroopers "
                    "is somewhere around here,"
                    " and has been terrifying the nearby ewok settlement.")
        print_pause("In front of you is a bunker.")
        print_pause("To your right is a destroyed AT-T fighter.")
        print_pause("In your hand you hold your trusty (but not "
                    "very effective) blaster.")

    elif planet == "Dagobah":
        print_pause("You find yourself standing in the middle the swamp, "
                    "surrounded by worrts and a few bogwing flying near by.")
        print_pause("Rumor has it that a sinister and powerful dark "
                    "force is somewhere around here, and you feel it near")
        print_pause("In front of you is a dark cave")
        print_pause("To your right is a crashed X-Wing")
        print_pause("In your hand you hold your trusty (but "
                    "not very effective) blaster.")


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand what you want to do.")
    return response


def fight(items):
    if "lightsaber" in items:
        if planet == "Tatooine":
            print_pause("As the raiders start shooting, "
                        "you unsheath your lightsaber.")
            print_pause("The lightsaber shines brightly in "
                        "your hand as you deflect the shots.")
            print_pause("You move to attack and start slaying "
                        "down all the Tusken Raiders")
            print_pause("You have rid the town of the "
                        "Tusken Raiders. You are victorious!")
            play_again()
        elif planet == "Endoor":
            print_pause("As the stormtroopers start shooting, "
                        "you unsheath your lightsaber.")
            print_pause("The lightsaber shines brightly in your "
                        "hand as you deflect the shots.")
            print_pause("You move to attack and start slaying "
                        "down all the stormtroopers")
            print_pause("You have liberated The Woods of Endor "
                        "from the Empire! You are victorious!")
            play_again()

        elif planet == "Dagobah":
            print_pause("As Vader moves to slay you, you "
                        "unsheath your lightsaber.")
            print_pause("The lightsaber shines brightly in "
                        "your hand as you deflect his attacks.")
            print_pause("You feel the Force in you and "
                        "start going on the offensive")
            print_pause("With the Force flowing strong within you, "
                        "you are able to disarm Vader")
            print_pause("He surrenders to you, and vows to help you "
                        "defeat the Emperor. You are victorious!")
            play_again()
    else:
        print_pause("You do your best...")
        print_pause("but your blaster is no match for the" + villain)
        print_pause("You have been defeated!")
        play_again()


def cave(items):
    if "lightsaber" in items:
        if planet == "Tatooine":
            print_pause("You inspect the crashed speedster.")
            print_pause("You've inspected it before, and found "
                        "the Luke's old lightsaber. "
                        "There is nothing else of value")
            print_pause("You walk back out to the dessert.")
            field(items)
        elif planet == "Endoor":
            print_pause("You inspect the destroyed AT-T.")
            print_pause("You've inspected it before, and found "
                        "the Luke's old lightsaber. "
                        "There is nothing else of value")
            print_pause("You walk back out to the woods.")
            field(items)

        elif planet == "Dagobah":
            print_pause("You inspect the crashed X-Wing.")
            print_pause("You've inspected it before, and found "
                        "the Luke's old lightsaber. "
                        "There is nothing else of value")
            print_pause("You walk back out to the swamp.")
            field(items)
    else:
        if planet == "Tatooine":
            print_pause("You inspect the crashed speedster.")
            print_pause("It turns out to be only a very old speedster.")
            print_pause("Your eye catches a glint of metal "
                        "underneath the seat")
            print_pause("You have found the lightsaber of Luke Skywalker!")
            print_pause("You discard your silly blaster and take "
                        "the lightsaber with you.")
            print_pause("You walk back out to the dessert.")
            items.append("lightsaber")
            field(items)
        elif planet == "Endoor":
            print_pause("You inspect the destroyed AT-T.")
            print_pause("It turns out to be only an old AT-T.")
            print_pause("Your eye catches a glint of metal "
                        "on the grass nearby")
            print_pause("You have found the lightsaber of Luke Skywalker!")
            print_pause("You discard your silly blaster and take "
                        "the lightsaber with you.")
            print_pause("You walk back out to the woods.")
            items.append("lightsaber")
            # field()
        elif planet == "Dagobah":
            print_pause("You inspect the crashed X-Wing.")
            print_pause("It turns out to be only a very X-Wing.")
            print_pause("Your eye catches a glint of metal "
                        "underneath the seat")
            print_pause("You have found the lightsaber of Luke Skywalker!")
            print_pause("You discard your silly blaster and take "
                        "the lightsaber with you.")
            print_pause("You walk back out to the swamp.")
            items.append("lightsaber")
            # field()
        field(items)


def house(items):
    if "lightsaber" not in items:
        if planet == "Tatooine":
            print_pause("You approach the door of the hut")
            print_pause("You are about to peek inside the hut when "
                        "hut opens and out steps a Tusken Raider.")
            print_pause("It's a trap! This hut is occupied by Tusken Raiders!")
            print_pause("The raiders attack you!")
            print_pause("You feel a bit outgunned, what with only "
                        "having a blaster")
        elif planet == "Endoor":
            print_pause("You approach the door of the bunker")
            print_pause("You are about to press the button to open it when "
                        "door opens and out steps a Stormtrooper.")
            print_pause("It's a trap! This bunker is the Empire's "
                        "last outpost!")
            print_pause("The stormtroopers aim at you!")
            print_pause("You feel a bit outgunned, what with only "
                        "having a blaster")

        elif planet == "Dagobah":
            print_pause("You approach the dark cave")
            print_pause("You are about to enter the cave when you see a "
                        "red flash and out steps Darth Vader.")
            print_pause("It's a trap! Darth Vader has ambushed you!")
            print_pause("Darth Vader attacks you!")
            print_pause("You feel a bit under-prepared for this, "
                        "what with only having a blaster")

    else:
        if planet == "Tatooine":
            print_pause("You approach the door of the hut")
            print_pause("You are about to peek isnide the hut when "
                        "hut opens and out steps a Tusken Raider.")
            print_pause("It's a trap! This hut is occupied by Tusken Raiders!")
            print_pause("The raiders attack you!")
        elif planet == "Endoor":
            print_pause("You approach the door of the bunker")
            print_pause("You are about to press the button to open when "
                        "door opens and out steps a Stormtrooper.")
            print_pause("It's a trap! This bunker is the Empire's "
                        "last outpost!")
            print_pause("The stormtroopers aim at you!")

        elif planet == "Dagobah":
            print_pause("You approach the dark cave")
            print_pause("You are about to enter the cave when you see a "
                        "red flash and out steps Darth Vader.")
            print_pause("It's a trap! Darth Vader has ambushed you!")
            print_pause("Darth Vader attacks you!")

    choice = valid_input("Would you like to (1) fight or (2) "
                         "run away?\n", "1", "2")
    if choice == '1':
        fight(items)
    elif choice == '2':
        print_pause("You run away. Luckily, you don't seem to have "
                    "been followed.")
        field(items)


def field(items):
    if planet == "Tatooine":
        choice = valid_input("Enter 1 to inspect the hut.\n"
                             "Enter 2 to investigate the crashed speedster.\n"
                             "What would you like to do?\n"
                             "(Please enter 1 or 2.)\n", "1", "2")
        if choice == '1':
            house(items)
        elif choice == '2':
            cave(items)
    elif planet == "Endoor":
        choice = valid_input("Enter 1 to inspect the bunker.\n"
                             "Enter 2 to investigate the destroyed AT-T.\n"
                             "What would you like to do?\n"
                             "(Please enter 1 or 2.)\n", "1", "2")
        if choice == '1':
            house(items)
        elif choice == '2':
            cave(items)
    elif planet == "Dagobah":
        choice = valid_input("Enter 1 to inspect the cave.\n"
                             "Enter 2 to investigate the crashed X-Wing.\n"
                             "What would you like to do?\n"
                             "(Please enter 1 or 2.)\n", "1", "2")
        if choice == '1':
            house(items)
        elif choice == '2':
            cave(items)


def play_again():
    response = valid_input("Would you like to go to another planet? "
                           "Please say 'yes' or 'no'.\n",
                           "yes", "no")
    if "no" in response:
        print_pause("OK, may the force be with you!")
    elif "yes" in response:
        print_pause("Very good, let's board the Millenium Falcon.")
        play_game()


def play_game():
    items = []
    intro()
    field(items)


play_game()
