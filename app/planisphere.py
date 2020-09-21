from random import randint

class Room(): 

    room_list = {}

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

        Room.room_list.update({name: self})
    
    def dead(self, death_scene):
        self.death = Room('Death', death_scene)

    def go(self, direction):
        return self.paths.get(direction)
    
    def add_paths(self, paths):
        self.paths.update(paths)
    
def name_room(room): 
    for key, value in Room.room_list.items():
        if value == room:
            return key

def set_error(room_name, player_input):
    if room_name == 'The Vault':
        
        if isinstance(player_input, int):
            error = 'BZZZZZZZZZD!'
        
        else:
            error = 'Not a valid input!'
    
    else:
        error = 'Not a valid input!'
    
    return error
        
main_entrance = Room("Main Entrance",
"""
You arrive at an ancient castle. You stand underneath a raised iron gate, with a wooden door towering above you, beckoning you in. 
To the side of the door is a lever, which upon first glance doesnt seem to be connected to anything.     
""")
main_entrance.dead("""The gate is suddenly released and impales you, good job...""")

the_hall = Room("The Hall",
"""
Upon entering the hall, you see a large rusted door to your west, a trapdoor by your feet and a staircase leading up.
""")
the_hall.dead("""You fall through the trapdoor onto a bed of sharp iron spikes, good job...""")

the_vault = Room("The Vault",
"""
As you approach the door, you realise it is a vault opening with a keypad sealing it shut. Faint blinking lights indicate a 3-digit passcode is required.
""")
the_vault.dead("""After too many erroneous attempts, the keypad blows up and kills you, good job...""")
code = f"{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}"

second_floor = Room("Second Floor",
"""
The staircase leads up to a small, dusty room, where you notice a fragment of a note lying in the corner. 
""")

second_floor.dead("""
You die...
""")

the_end = Room("The End",
"""
As the vault creaks open, you catch a glimpse of a faint shimmer of blue. 
You soon realise you are at one end of a portal, with the other end but a mystery. 
Your curiosity gets the better of you and you leap inside...
(to be continued)
""")

second_floor.add_paths({
    'i go downstairs': the_hall,
    'i go down': the_hall,
    'i go back': the_hall,
    'i go hall': the_hall,
    'i grab note': code,
    'i look note': code,
    'i get note': code,
    'i take note': code,  
    'i read note': code,
    'i pick up': code
})

the_hall.add_paths({
    'i open trapdoor': the_hall.death,
    'i go trapdoor': the_hall.death,
    'i climb stairs': second_floor,
    'i go stairs': second_floor, 
    'i go upstairs': second_floor,
    'i go up': second_floor,
    'i go north': second_floor, 
    'i go west': the_vault,
    'i go door': the_vault,
    'i go vault': the_vault,
    'i go back': main_entrance,
    'i go south': main_entrance,
    'skip': second_floor
})

the_vault.add_paths({
    code: the_end,
    'i go hall': the_hall,
    'i go east': the_hall,
    'i go back': the_hall,
    '*': the_vault.death
})

main_entrance.add_paths({
    'i pull lever': main_entrance.death,
    'i go door': the_hall,
    'i open door': the_hall,
    'i go inside': the_hall,
    'i enter door': the_hall,
    'i enter': the_hall 
})

START = 'Main Entrance'


