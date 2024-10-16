# Example
# This a project I found online that's similar to what I want to do
# Not my work

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

class Player(object):
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []

class Item(object):
    def __init__(self, name, description, is_movable):
        self.name = name
        self.description = description
        self.is_movable = is_movable

# Create items
# Closet Items
shelf = Item("shelf", "The shelf is empty.", False)
uniform = Item("uniform", "The uniform is blue and drab.", True)
        
# Control Room Items
guard = Item("guard", "The guard looks mean and menacing.", False)
electronic_lock = Item("lock", "The lock is in front of a large door to the east.", "False")
id = Item("id", "The id is silver with a barcode on it.", True)

# Airlock Items
spacesuit = Item("spacesuit", "The spacesuit looks old, but safe.", True)
button = Item("button", "The big red button has a warning symbol on it.", False)

# Create Rooms
# Closet
closet = Room("The Closet", "You are in a small nondescript closet.")
closet.items.append(shelf)
closet.items.append(uniform)

# Control Room
control_room = Room("The Control Room", "You are in a small room that looks like it controls something. There is an airlock to the east.")
control_room.items.append(guard)
control_room.items.append(electronic_lock)
control_room.items.append(id)

# Airlock
airlock = Room("The Airlock", "You are in a small room that is clearly an airlock. There is a window to space in the east. There is an airlock door to the west.")
airlock.items.append(spacesuit)
airlock.items.append(button)

# Create exits
closet.exits["n"]= control_room
control_room.exits["s"] = closet
airlock.exits["w"] = control_room

# Create the player
player = Player("The Player", closet)

# Start game
print("Welcome to My Space Adventure")
print("\nYou wake up on a space station.")

while True:
    print("")
    print(player.location.name)
    print(player.location.description)
    print("\nHere are the exits: ")
    for exit in player.location.exits:
        print(exit)
    print("\nYou see the following: ")
    for item in player.location.items:
        print(item.name)
        
    # Get command
    try:
        # Python 2.7
        command = raw_input("\n> ")
    except:
        # Python 3.x
        command = input("\n> ")
        
    words = command.split()
    if len(words) > 0:
        verb = words[0]
    if len(words) > 1:
        noun = words[1]
    
    # Examine
    if verb == "examine":
        for item in player.location.items:
            if item.name == noun:
                print(item.description)
        for item in player.inventory:
            if item.name == noun:
                print(item.description)

    # Get
    if verb == "get":
        for item in player.location.items:
            if item.name == noun:
                # Check is it movable
                if item.is_movable:
                    print("You take the {}".format(item.name))
                    # Remove from room
                    player.location.items.remove(item)
                    # Add to player's inventory
                    player.inventory.append(item)
                
                else:
                    print("Sorry, you can't move that.")

    # Drop
    if verb == "drop":
       for item in player.inventory:
            print("You drop the {}.".format(item.name))
            player.inventory.remove(item)
            player.location.items.append(item)
        
    # Inventory
    if verb in ["inv", "inventory"]:
        print("You have the following: ")
        for item in player.inventory:
            print(item.name)

    # Movement
    if verb in ["n", "s", "e", "w", "u", "d"]:
        if verb in player.location.exits:
            player.location = player.location.exits[verb]
            print("You go {} and find yourself in a new room.".format(verb))
            

    # Room specific code
    # Control Room
    if player.location == control_room:
        if uniform not in player.inventory:
            print("The guard sees you. Without saying a word, he pulls his laser gun and kills you. Game over.")
            exit()
        else:
            print("The guard looks up, looks at the uniform, and turns his head back to the display.")

    if player.location == control_room:
        if verb == "open" and noun == "airlock":
            if id in player.inventory:
                print("You swipe the id and the airlock opens.")
                control_room.exits["e"] = airlock
                
            else:
                print("The airlock won't open. You must need some id to open it.")

    # Airlock
    if player.location == airlock:
        if "w" in airlock.exits:
            del(airlock.exits["w"])
            print("The airlock door closes! You are trapped.  There is no lock on this side.")
            
    if player.location == airlock:
        if verb == "press" and noun == "button":
            if spacesuit in player.inventory:
                print("You put on the spacesuit and push the red button.")
                print("The outer airlock door opens!")
            else:
                print("The outer airlock door opens.  You are sucked into the vacuum of space and die.")
                exit()
