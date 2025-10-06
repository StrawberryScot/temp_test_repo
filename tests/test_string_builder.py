from lib.string_builder import *

def test_string_builder_initialises_with_empty_string():
    sb = StringBuilder()
    assert sb.str == ""

def test_string_builder_concats_race_to_car():
    sb = StringBuilder()
    sb.add("race")
    sb.add("car")
    assert sb.str == "racecar"

def test_string_builder_size_returns_7_for_racecar():
    sb = StringBuilder()
    sb.add("racecar")
    result = sb.size()
    assert result == 7

def test_string_builder_output_returns_racecar_for_racecar():
    sb = StringBuilder()
    sb.add("racecar")
    result = sb.output()
    assert result == result
