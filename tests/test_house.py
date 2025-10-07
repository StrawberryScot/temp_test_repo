from lib.house import *
import pytest

def test_house_attributes():
    my_house = House(137, "white")
    assert my_house.floors == 2
    assert my_house.number ==137
    assert my_house.door_color =="white"

def test_get_details():
    my_house = House(137, "white")
    assert my_house.get_details() == "House number 137 has 2 floors and a white door"

def test_repaint_door():
    my_house = House(137, "white")
    my_house.repaint_door("blue")
    assert my_house.door_color == "blue"
