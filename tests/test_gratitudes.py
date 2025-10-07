from lib.gratitudes import *

def test_gratitudes_initialises_with_empty_list():
    grats = Gratitudes()
    assert grats.gratitudes == []

def test_gratitudes_appends_love_to_empty_list():
    grats = Gratitudes()
    grats.add("love")
    assert grats.gratitudes == ["love"]

def test_gratitudes_returns_love_formatted():
    grats = Gratitudes()
    grats.add("love")
    result = grats.format()
    assert result == "Be grateful for: love"

def test_gratitudes_returns_love_and_family_formatted():
    grats = Gratitudes()
    grats.add("love")
    grats.add("family")
    result = grats.format()
    assert result == "Be grateful for: love, family"
