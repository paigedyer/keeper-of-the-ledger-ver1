'''Paige Dyer'''

'''dictrooms = {'Courtyard': {'go north': 'Barn'},
         'Barn': {'go north': 'Cave', 'go south': 'Courtyard', 'go east': 'Meadow', 'go west': 'Wardrobe'},
         'Wardrobe': {'go north': 'Burning Forest', 'go east': 'Barn'},
         'Cave': {'go south': 'Barn', 'go west': 'Burning Forest'},
         'Burning Forest': {'go south': 'Wardrobe', 'go east': 'Cave'},
         'Meadow': {'go east': 'Pit', 'go west': 'Barn'},
         'Pit': {'go west': 'Meadow', 'go south': 'Final'},
         'Final': 'None'
         }'''

''' I made a dictionary here of the rooms because I know it is a requirement, but I had written so much of the code already with lists that if I incorporated 
a dictionary it would require me to rewrite so much of the code. It would be in a more efficient way, but I just didn't have enough time to rewrite and debug all new code.'''

import sys
import random

room_list = ['Courtyard', 'Barn', 'Wardrobe', 'Burning Forest', 'Cave', 'Meadow', 'Pit', 'Final'] #No Null needed here because Courtyard is a room

character_list = ['Null',  #Adding Null so when referencing indices all are the same
                  'Oliver the Upright Hog',
                  'Dominique the Succubus',
                  'Cinder the Eternal Fire',
                  'Mortas Sanguine the Vampiric Lord',
                  'Blossom the Nymph Queen',
                  'Dray the Bottomless Pit',
                  'The Keeper of the Ledger']

character_dialogue = ['Null', #Adding Null so when referencing indices all are the same
                      'You see a strange character that appears to be half pig half man.',
                      'You see a tall woman with dark features, you try to look away but find her entrancing.',
                      'You see no humanoid figure, but instead feel an immense and hot energy around you',
                      'You see a tall and slender man. His skin looks to be made of rock and his eyes are sunken deeply into his skull. He looks up at you and your stomach falls to your feet, a feeling you\'ve never experienced before',
                      'You see a woman with massive wings quickly move between branches along the clearing\'s edge.',
                      'A loud and penetrating voice emerges from no particular location, it seems as if it\'s coming from inside of you.']

item_list = ['Null', #Adding Null so when referencing indices all are the same
             'Shard 1: Irony', 'Shard 2: Love and Desire', 'Shard 3: Consequence', 'Shard 4: Fear', 'Shard 5: The Plants and Animals', 'Shard 6: The After']

_current_inventory_ = [] # initialize inventory being empty
current_location = room_list[0] # sets current location to courtyard in the beginning

def _instructions_(): # User can call this during game to recall instructions
    print('Instructions: ')
    print("Travel through all rooms in the Labyrinth to find and collect all 6 shards of the Soulbreaker Dagger.")
    print("Once you have collected all 6 shards, find the Keeper of the Ledger and defeat him.")
    print()

def _commands_(): # Travel and collect items
    print('Type "go north, go south, go east, go west" to travel in a direction.')
    print('Type "speak" to speak to someone')
    print('Type "help" at any time to view this list of commands again')
    print('Type "inventory" at any time to view your current inventory')
    print()

def _introduction_():
    print("You've arrived at the Labyrinth, enter if you wish.")
    print()

def _room_(room, character, dialogue, item): #use whenever the player enters a new room
    global _current_inventory_
    global _next_action_
    length = len(_current_inventory_)
    global current_location
    current_location = room
    while True:
        if current_location == room:
            print('You are in the {}'.format(room))
            if length == 0:
                print('[Nothing in inventory]')
            else:
                print('Current inventory: ', _current_inventory_)
        if item not in _current_inventory_:
            print(dialogue)
        if item in _current_inventory_:
            print('The figure from before seems to have vanished...')
        _next_action_ = input('What to do next? \n')
        if _next_action_ == 'speak':
            if item not in _current_inventory_:
                _current_inventory_.append(item)
                print('You meet {}. They teach you their knowledge and you gain {}.'.format(character, item))
                _next_action_ = input('Where do you want to go next? \n')
                _movement_()
            elif item in _current_inventory_: #reminds user they've already been here
                print('There is no one except yourself here to speak to.')
        if _next_action_ == 'go north' or _next_action_ == 'go south' or _next_action_ == 'go west' or _next_action_ == 'go east':
            if item not in _current_inventory_:
                _verify_ = input('Leave without speaking? (Y/N)? \n') #verify that user doesn't want to speak to character
                if _verify_ == 'Y' or _verify_ == 'y':
                    _movement_()
                if _verify_ == 'N' or _verify_ == 'n':
                    _next_action_ = 'speak'
            if item in _current_inventory_: #if they've already collected the item they just move along
                _movement_()
        elif _next_action_ == 'help':
            _instructions_()
            _commands_()
        elif _next_action_ == 'inventory':
            if len(_current_inventory_) == 0:
                print('[Nothing in inventory]')
            else:
                print('Current inventory: {}'.format(_current_inventory_))
        else:
            print('Invalid input. Try typing "speak".')
            continue

def courtyard(): # courtyard only, no character to speak to
    global _current_inventory_
    global current_location
    global _next_action_
    current_location = room_list[0]
    print('You are in the {}.'.format(current_location))
    length = len(_current_inventory_)
    if length == 0:
        print('[Nothing in inventory]')
    else:
        print('Current inventory: ', _current_inventory_)
    _next_action_ = input('What to do next? \n')
    if _next_action_ == 'go north' or _next_action_ == 'go south' or _next_action_ == 'go west' or _next_action_ == 'go east':
        _movement_()
    elif _next_action_ == 'speak':
        speakran()
        _next_action_ = input('What to do next? \n')
    elif _next_action_ == 'help':
        _instructions_()
        _commands_()
        _next_action_ = input('What to do next? \n')
    elif _next_action_ == 'inventory':
        print(_current_inventory_)
        _next_action_ = input('What to do next? \n')


def speakran(): # for trying to speak at wrong time, prints a random response.
    speak1 = 'You cannot speak right now. Try entering a direction.'
    speak2 = 'You either have no one to speak to or have already spoken to this figure. Try typing something like "go north" or "go south"?'
    speak3 = 'You want to speak but can\'t. It\'s almost like the universe is telling you to go somewhere instead of speaking right now.'
    speak4 = 'You try to speak but nothing comes out. Try entering a direction. Or you could try speaking again and see how that works out for you...'
    speaklist = [speak1, speak2, speak3, speak4]
    speakresponse = random.choice(speaklist)
    print(speakresponse)

def _final_(): #boss room win or lose
    global _current_inventory_
    global _next_action_
    global current_location

    print('You walk into the largest room you\'ve ever seen. You are standing on a stone balcony with moss and vines growing over the railings.')
    print('At the center of the room is a structure that has no certain shape. You can\'t tell if it\'s a creature or a building of some kind.')
    print()
    while True:
        _next_action_ = input('Press enter \n')
        print()
        if _next_action_ == '' \
                            '':
            if len(_current_inventory_) == 6:
                _won_()
            if len(_current_inventory_) < 6:
                _lost_()
        else: #validates input
            print('Invalid input.')
            continue

def _won_():
    global current_location
    global _current_inventory_
    global _next_action_
    print('You collected all 6 pieces of the Soulbinder Dagger and defeated The Keeper of the Ledger and '
          'have gained immortal life.'
          'YOU WON! :D')
    _next_action_ = input('Play again? (Y\\N)')
    print()
    if _next_action_ == 'N' or _next_action_ == 'no' or _next_action_ == 'n':
        print('Thanks for playing!')
        sys.exit()
    elif _next_action_ == 'Y' or _next_action_ == 'yes' or _next_action_ == 'y':
        current_location = 'Courtyard'
        _current_inventory_ = []
        _introduction_()
        _instructions_()
        _commands_()
        _next_action_ = input('What to do next? \n')
        _movement_()
    else:
        print('Invalid input. Try saying "Y" or "N"?')

def _lost_():
    global _next_action_
    global current_location
    global _next_action_
    global _current_inventory_
    print('The Keeper of the Ledger raises a long arm and in one movement he crushes you instantly.')
    print('You failed to collect all 6 pieces of the Soulbinder Dagger and were defeated by The Keeper of the Ledger.')
    print('YOU LOST! :(')
    _next_action_ = input('Try again? (Y\\N)')
    print()
    if _next_action_ == 'N' or _next_action_ == 'no' or _next_action_ == 'n': #if user enters uppercase or lowercase or spells out "no" or "yes"
        print('Thanks for playing!')
        sys.exit()
    elif _next_action_ == 'Y' or _next_action_ == 'yes' or _next_action_ == 'y':
        current_location = 'Courtyard'
        _current_inventory_ = []
        _introduction_()
        _instructions_()
        _commands_()
        _next_action_ = input('What to do next? \n')
        _movement_()
    else:
        print('Invalid input. Try saying "Y" or "N"?')

def _movement_(): #main function
    global current_location
    global _next_action_
    while True:
        if _next_action_ == 'help': # get instructions and commands
            _instructions_()
            _commands_()
            print('You are in the {}.'.format(current_location))
            _next_action_ = input('What to do next? \n')
        elif _next_action_ == 'inventory': # view current inventory
            print(_current_inventory_)
            _next_action_ = input('What to do next? \n')
        elif _next_action_ == 'go north': # directions start here
            if current_location == 'Courtyard':
                _room_(room_list[1], character_list[1], character_dialogue[1], item_list[1])
            elif current_location == 'Barn':
                _room_(room_list[4], character_list[4], character_dialogue[4], item_list[4])
            elif current_location == 'Wardrobe':
                _room_(room_list[3], character_list[3], character_dialogue[3], item_list[3])
            else:
                print('You cannot go that way')
                print('You are in the {}.'.format(current_location))
                _next_action_ = input('What to do next? \n')
        elif _next_action_ == 'go south':
            if current_location == 'Barn':
                courtyard()
            elif current_location == 'Burning Forest':
                _room_(room_list[2], character_list[2], character_dialogue[2], item_list[2])
            elif current_location == 'Pit':
                _final_()
            elif current_location == 'Cave':
                _room_(room_list[1], character_list[1], character_dialogue[1], item_list[1])
            else:
                print('You cannot go that way')
                print('You are in the {}.'.format(current_location))
                _next_action_ = input('What to do next? \n')
        elif _next_action_ == 'go west':
            if current_location == 'Barn':
                _room_(room_list[2], character_list[2], character_dialogue[2], item_list[2])
            elif current_location == 'Cave':
                _room_(room_list[3], character_list[3], character_dialogue[3], item_list[3])
            elif current_location == 'Meadow':
                _room_(room_list[1], character_list[1], character_dialogue[1], item_list[1])
            elif current_location == 'Pit':
                _room_(room_list[5], character_list[5], character_dialogue[5], item_list[5])
            else:
                print('You cannot go that way')
                print('You are in the {}.'.format(current_location))
                _next_action_ = input('What to do next? \n')
        elif _next_action_ == 'go east':
            if current_location == 'Barn':
                _room_(room_list[5], character_list[5], character_dialogue[5], item_list[5])
            elif current_location == 'Meadow':
                _room_(room_list[6], character_list[6], character_dialogue[6], item_list[6])
            elif current_location == 'Wardrobe':
                _room_(room_list[1], character_list[1], character_dialogue[1], item_list[1])
            elif current_location == 'Burning Forest':
                _room_(room_list[4], character_list[4], character_dialogue[4], item_list[4])
            else:
                print('You cannot go that way')
                print('You are in the {}.'.format(current_location))
                _next_action_ = input('What to do next? \n')
        elif _next_action_ == 'speak':
            speakran()
            _next_action_ = input('What to do next? \n')
        else:
            _next_action_ = input('Invalid input. Try entering a direction. If you need help, type "help". \n')


_introduction_()
_instructions_()
_commands_()
print('You are in the {}'.format(current_location))
_next_action_ = input('What to do next? \n')
_movement_()
