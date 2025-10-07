from lib.house import *
import pytest

def test_house_instantiates_with_floor_attribute_set_to_2():
    my_house = House()
    assert my_house.floors == 2
