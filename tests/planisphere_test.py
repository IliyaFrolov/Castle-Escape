import pytest
from gothonweb.planisphere import *

def test_room():
    gold = Room("GoldRoom",
                """ This room has gold in it you can grab.
                door to the north.""")

    assert gold.name == "GoldRoom", 'Name should be GoldRoom'

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert center.go('north') == north
    assert center.go('south') == south

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")  
    
    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})  
    
    assert start.go('west') == west
    assert start.go('west').go('east') == start
    assert start.go('down').go('up') == start

def test_descriptions():

    start = Room("Celler", "This is a dark and smelly cellar.")

    assert start.description == "This is a dark and smelly cellar."

def test_gothon_game_map():
    start_room = load_room(START)
    
    assert start_room.go('shoot!').description == """Wrong action! The Gothon blasts you, turning you into soup!"""
    assert start_room.go('dodge!') == start_room.death

    laser_room = start_room.go('tell a joke')

    assert laser_room == laser_weapon_armory
    assert laser_room.go('skip') == the_bridge
    assert laser_room.go('*') == laser_room.death   

def test_load_room():
    assert load_room(START) == central_corridor

def test_name_room():
    assert name_room('central_corridor') == 'START'
    assert name_room(central_corridor) == 'central_corridor'

    
    










