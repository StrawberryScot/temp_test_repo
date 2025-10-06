from lib.report_length import *

def test_report_length_returns_formatted_six_for_burger():
    result = report_length("burger")
    assert result == "This string was 6 characters long."

def test_report_length_returns_formatted_eight_for_elephant():
    result = report_length("elephant")
    assert result == "This string was 8 characters long."
