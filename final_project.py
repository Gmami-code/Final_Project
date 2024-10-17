# Print welcome message to start the game
def start():
    str(input("Type 'start' to begin the adventure: "))
    if input == 'start':
        return(storyline())
    else: 
        str(input("Invalid choice. Please type 'start' to begin the adventure: "))

# Print storyline
def storyline():
# Write storyline here
    print("With what you know now, you have a choice.")
    print() # Prints an empty line
    print("The Right Path or The Left Path?")
    str(input("Type 'right' or 'left': "))
    if input == 'right':
        return (first_right_path())
    elif input == 'left':
        return (first_left_path())
    else:
        str(input("Invalid choice. Please type 'right' or 'left' to choose a path: "))


def first_right_path():


def first_left_path():


# def second_right_path():


# def second_left_path():


# def third_right_path():


# def third_left_path():


# def victory(): # Correct path


# def game over(): # ?
