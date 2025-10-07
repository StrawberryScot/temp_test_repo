from lib.house import *
import pytest

def test_house_attributes():
    my_house = House(137, "white")
    assert my_house.floors == 2
    assert my_house.number ==137
    assert my_house.door_color =="white"
