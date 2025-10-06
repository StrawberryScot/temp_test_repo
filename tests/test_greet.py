from lib.greet import *

def test_greet_returns_hello_bob_for_bob():
    result = greet("bob")
    assert result == "Hello, bob"
