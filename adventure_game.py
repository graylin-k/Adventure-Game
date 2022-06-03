import time
import random


def print_pause(dialogue):
    print(dialogue)
    time.sleep(2)


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid.')


def introduction():
    print_pause("\nYou are suddenly awoken from your hypnotic slumber."
                "\n\nThe thumping of metal colliding with wood, \ncombined"
                " with an abnormal sensation of heat, \nrush over you.")
    print_pause("\nNow, fully awakened from your stupor,"
                " you remember where you are...")
    print_pause("\nYou are a buccaneer and your ship\'s deck is on fire"
                "\nand is being hit by a barrage of cannon ball fire.")
    print_pause("\nYou are in the belly of the ship.")
    print_pause("\nIt is imperative for you to act fast.")


def belly_of_ship(random_noun, talisman):
    print_pause("\nEnter (1) to find a lifeboat or enter"
                "(2) to join your crew...")
    print_pause("\nWhat shall your choice be ye sailor?")
    choice_1 = valid_input("(Please enter 1 or 2)", ['1', '2'])
    if choice_1 == "1":
        lifeboat(random_noun, talisman)
    else:
        join_crew(random_noun, talisman)


def lifeboat(random_noun, talisman):
    print_pause("\nYou finally spot a lifeboat that is intact.")
    print_pause("\nAs you approach the lifeboat and peer over the edge,\n"
                "a " + random_noun + " is there and is ready to attack!")
    print_pause("\nThe " + random_noun + " lunges out to attack you!")
    choice_2 = valid_input("\nWould you like to (1) fight or"
                           " (2) turn back to the belly of the ship?",
                           ['1', '2'])
    if choice_2 == "1":
        if "cutlass" in talisman:
            print_pause("\nAs the " + random_noun + " lunges out to"
                        " attack you,"
                        "\nyou wield your cutlass ready to defend your"
                        " crew.")
            print_pause("\nThe " + random_noun +
                        " sees your crew and your cutlass."
                        "\n\nThe " + random_noun +
                        " then promptly decides to jump overboard!")
            print_pause("\nYou and your crew take the lifeboat to safety,"
                        " \nfar away from your burning ship.")
            print_pause("\nCongratulations!\n"
                        "You have successfully navigated this situation!")
        else:
            print_pause("\nYou try to ward off the " + random_noun +
                        " with just your bare hands to no avail.")
            print_pause("\nUnfortunately,"
                        " this marks the end of your adventure.")
            print_pause("\nMaybe try staying with your crew the next time."
                        "\n")
        restart_game()
    else:
        print_pause("\nYou aptly turn around and head back"
                    " to the belly of the ship.")
        belly_of_ship(random_noun, talisman)


def join_crew(random_noun, talisman):
    if "cutlass" in talisman:
        print_pause("\nYour crew is starting to"
                    " question your decision making.")
        print_pause("\nThey wonder why you have decided to turn back"
                    " to the burning ship,"
                    "\ninstead of fighting your way out with the cutlass"
                    " they gave you.")
        print_pause("\nYou head back to the belly of the ship.")
    else:
        print_pause("\nYour crew is relieved to see that you have finally"
                    " decided to join them.")
        print_pause("\nThey see that you have come empty handed.")
        print_pause("\nThey promptly give you the sharpest cutlass around.")
        print_pause("\nYou and your crew run back to the belly of the ship to"
                    " make a escape plan.")
        talisman.append("cutlass")
    belly_of_ship(random_noun, talisman)


def start_game():
    random_noun = random.choice(["tiger", "shark", "bandit"])
    talisman = []
    introduction()
    belly_of_ship(random_noun, talisman)


def restart_game():
    print_pause("\nWould you like to restart the game?")
    choice_last = valid_input("\n(Please enter Yes or No...)",
                              ['Yes', 'No']).lower()
    if choice_last == 'Yes':
        start_game()
    else:
        quit()


start_game()
