import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

##### Player Setup #####
class player:
	def __init__(self):
		self.name = ''
		self.hp = 0
		self.mp = 0
		self.status_effects = []
		self.location = 'start'


myPlayer = player()

##### Title Screen #####
def title_screen_selections():
	option = input("> ")
	if option.lower() == ("play"):
		start_game() #placeholder until written
	elif option.lower() == ("help"):
		help_menu()
	elif option.lower() == ("quit"):
		sys.exit()
	while option.lower() not in ['play', 'help', 'quit']:
		print("Please enter a valid command")
		option = input("> ")
		if option.lower() == ("play"):
			start_game() #placeholder until written
		elif option.lower() == ("help"):
			help_menu()
		elif option.lower() == ("quit"):
			sys.exit()


def title_screen():
	os.system('cls' if os.name == 'nt' else 'clear')
	print('#############################')
	print('# Welcome to this Text RPG! #')
	print('#############################')
	print('           - Play -          ')
	print('           - Help -          ')
	print('           - Quit -          ')
	title_screen_selections()

def help_menu():
	print('#############################')
	print('# Welcome to this Text RPG! #')
	print('#############################')
	print('- Use up, down, left, right to move')
	print('- Type your commands to execute them')
	print('- Use "look" to inspect something')
	title_screen_selections()


##### Game Functionality #####
def start_game():


##### Map #####

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False
                 'b1': False, 'b2': False, 'b3': False, 'b4': False
                 'c1': False, 'c2': False, 'c3': False, 'c4': False
                 'd1': False, 'd2': False, 'd3': False, 'd4': False
                }

zonemap = {
    'a1': {
        ZONENAME: '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
        },
    'a2': {
        ZONENAME: '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
        },
    'a3': {
        ZONENAME: '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
        },
    'a4': {
        ZONENAME: '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
        },
    'b1': {
        ZONENAME: '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
        },
    'b2': {
        ZONENAME: 'Home',
        DESCRIPTION = 'This is your Home!'
        EXAMINATION = 'Your home looks the same, nothing has changed'
        SOLVED = False
        UP = 'a2',
        DOWN = 'c2',
        LEFT = 'b1'
        RIGHT = 'b3'
        },
    'b3': {
        ZONENAME: '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
        },
    'b4': {
        ZONENAME: '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
        },
    'c1': {
        ZONENAME: '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
        },
    'c2': {
        ZONENAME: '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
        },
    'c3': {
        ZONENAME: '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
        },
    'c4': {
        ZONENAME: '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
        },
    'd1': {
        ZONENAME: '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
        },
    'd2': {
        ZONENAME: '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
        },
    'd3': {
        ZONENAME: '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
        },
    'd4': {
        ZONENAME: '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
        },
	
          }
