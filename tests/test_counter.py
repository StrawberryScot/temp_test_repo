from lib.counter import *

def test_counter_initialises_with_a_count_of_zero():
    counter = Counter()
    assert counter.count == 0

def test_counter_adds_four_for_four():
    counter = Counter()
    counter.add(4)
    assert counter.count == 4
    result = counter.report()
    assert result == "Counted to 4 so far."

def test_counter_adds_eight_for_six_plus_two():
    counter = Counter()
    counter.add(6)
    counter.add(2)
    assert counter.count == 8
    result = counter.report()
    assert result == "Counted to 8 so far."


