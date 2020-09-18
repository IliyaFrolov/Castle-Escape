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
You arrive at a castle. The gate is suspended open, with a door seemingly leading
inside. To the side of the door is a lever, which upon first glance, doesnt seem 
to be connected to anything.     
""")
main_entrance.dead("""The gate suddenly drops and impales you, good job...""")

the_hall = Room("The Hall",
"""
Upon entering the hall, you see a big door to your west, a trapdoor nearby and a staricase 
leading up.
""")
the_hall.dead("""You fall through the trapdoor, which has spikes beneath, good job...""")

the_vault = Room("The Vault",
"""
The door has a keypad to the side, requiring a 3 digit passcode.
""")
the_vault.dead("""After many wrong tries, the keypad blows up and you die, good job...""")
code = f"{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}"

second_floor = Room("Second Floor",
"""
The staircase leads to a small dark room, with a tiny note laying in the corner. 
""")

second_floor.dead("""
You die
""")

the_end = Room("The End",
"""
As you open the vault, you see a faint shimmer of blue. Within the vault is a portal,
unknown where it leads to. Your curiosity gets the best of you and you jump inside...
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
    'i read note': code
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
    'skip': the_hall
})

START = 'Main Entrance'


