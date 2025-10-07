from lib.present import *
import pytest

def test_wrap_and_then_unwrap():
    present = Present()
    present.wrap(21)
    assert present.unwrap() == 21

def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    message = str(e.value)
    assert message == "No contents have been wrapped."

def test_wrapping_already_wrapped():
    present = Present()
    present.wrap(21)
    with pytest.raises(Exception) as e:
        present.wrap(32)
    message = str(e.value)
    assert message == "A contents has already been wrapped."

