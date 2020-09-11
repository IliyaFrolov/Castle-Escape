from random import randint

class Room(): 

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
    
    def dead(self, death_scene):
        self.death = Room('death', death_scene)

    def go(self, direction):
        return self.paths.get(direction)
    
    def add_paths(self, paths):
        self.paths.update(paths)
    
def load_room(name):
    """
    There is a potential security problem here. 
    Who gets to set name? Can that expose a variable?
    """
    return globals().get(name)

def name_room(room):
    """
    Same possible security probelm. Can you trust the room?
    What's better solution than this globals lookup?
    """
    for key, value in globals().items():
        if value == room:
            return key

def set_error(room_name):
    if room_name == 'main_entrance':
        error = 'Not a valid input!'

    elif room_name == 'the_hall':
        error = 'Not a valid input!'
    
    elif room_name == 'the_vault':
        error = 'BZZZZZZZZZD!'
    
    elif room_name == 'second_floor':
        error = 'Not a valid input!'
    
    return error
        
main_entrance = Room("Entrance",
"""
You arrive at a castle. The gate is suspended open, with a door seemingly leading
inside. To the side of the door is a lever, which upon first glance, doesnt seem 
to be connected to anything.     
""")
main_entrance.dead("""The gate suddenly drops and impales you, good job...""")

the_hall = Room("Main hall",
"""
Upon entering the hall, you see a big door to your west, a trap door nearby and a staricase 
leading up.
""")
the_hall.dead("""You fall through the trapdoor, which has spikes beneath, good job...""")

the_vault = Room("Big door with keypad",
"""
The door has a keypad to the side, requiring a 3 digit passcode.
""")
the_vault.dead("""After many wrong tries, the keypad blows up and you die, good job...""")
code = f"{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}"

second_floor = Room("Second floor",
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
    'i look note': code,
    'i take note': code  
})

the_hall.add_paths({
    'i open trapdoor': the_hall.death,
    'i go trapdoor': the_hall.death,
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
    'skip': the_hall
})

START = 'main_entrance'


