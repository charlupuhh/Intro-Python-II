from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

sword = Item('sword', "a bit dull, but it'll get the job done")
shield = Item('shield', "it's quite sturdy")
loot = Item('loot', 'a bag of gold')
ruby = Item('ruby', 'a glowing stone')

room['outside'].contents.append(sword)
room['outside'].contents.append(shield)
room['treasure'].contents.append(loot)
room['treasure'].contents.append(ruby)
#
# Main
#
# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
action_error = '''
                Please enter a valid command:
                    grab [item]: pickup an item
                    drop [item]: drop an item                    
                    n: move north
                    e: move east
                    s: move south
                    w: move west
                    q: quit the game
                '''

def room_adventure():
    print("Let's adventure!")
    playing = True
    player = Player("Charlie", room['outside'])

    while playing:
        print(f"Your are now at the {player.current_room.name}")
        print(f"Your inventory contents are")
        for i in player.inventory:
            print(f"a {i.name}")
        print(f"You look around you and see")
        for i in player.current_room.contents:
            print(f"a {i.name} - {i.description}")
        print(f"{player.current_room.description}")
        action = input("What is your move?").split()
        print("\n")

        if len(action) == 1:
        # Quit if action is Q
            action = action[0]
            if action == "q":
                print("Best of luck in your future journies")
                playing = False
            elif action == "n":
                try:
                    player.current_room = player.current_room.n_to
                except:
                    print("There is an obstacle in your way, try a different direction")
            elif action == "e":
                try:
                    player.current_room = player.current_room.e_to
                except:
                    print("There is an obstacle in your way, try a different direction")
            elif action == "s":
                try:
                    player.current_room = player.current_room.s_to
                except:
                    print("There is an obstacle in your way, try a different direction")
            elif action == "w":
                try:
                    player.current_room = player.current_room.w_to
                except:
                    print("There is an obstacle in your way, try a different direction")
            else:
                print(action_error)
        elif len(action) == 2:
            thing = action[1]
            action = action[0]
            if action == 'grab':
                for i in player.current_room.contents:
                    if thing == i.name:
                        print(f"You grab the {thing}")
                        player.current_room.remove_item(i)
                        player.grab_item(i)
            elif action == 'drop':
                for i in player.inventory:
                    if thing == i.name:
                        print(f"You drop the {thing}")
                        player.current_room.add_item(i)
                        player.drop_item(i)
            else:
                print(action_error)
        else:
            print(print(action_error))


room_adventure()