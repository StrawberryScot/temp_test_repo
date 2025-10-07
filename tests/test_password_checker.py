from lib.password_checker import *
import pytest

def test_check_returns_true_for_12345678():
    pc = PasswordChecker()
    assert pc.check("12345678") == True

def test_check_raises_exception_for_1234567():
    pc = PasswordChecker()
    with pytest.raises(Exception) as e:
        pc.check("1234567")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

