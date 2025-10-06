from lib.check_codeword import *

def test_check_codeword_returns_wrong_for_abracadabra():
    result = check_codeword("abracadabra")
    assert result == "WRONG!"

def test_check_codeword_returns_close_for_hose():
    result = check_codeword("hose")
    assert result == "Close, but nope."

def test_check_codeword_returns_correct_for_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."


