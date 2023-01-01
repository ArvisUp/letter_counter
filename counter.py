""" Counts letters in user input. 
btw I wanted to use dictionaries, not set() and list"""

print("This will take whatever you write and count all the letters in it.")
user_input = input("Enter something: ")
character_dictionary = {}
char_lenght = {}
sorted_character_dictionary = {}


def sorter():
    """ Sorts user input in dictionaries by letters"""

    for i in user_input.lower():
        # Loops through user_input checking for letters, discarding all the other characters

        if str(i).isalpha():
            if f"{i}" in character_dictionary:
                character_dictionary[i].append(i)
            else:
                character_dictionary[i] = [i]


def sort_and_count():
    # Sorts character dictionary and counts letters
    sorted_character_dictionary = dict(sorted(character_dictionary.items()))
    for key in sorted_character_dictionary:
        print("Letter", key.upper(), "was used:",  len(
            sorted_character_dictionary[key]), "times.")


sorter()
sort_and_count()
