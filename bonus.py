import re


def add_string(string):
    result = 0
    for s in re.split('\W+', string):
        if s.isdigit() and int(s) <= 1000:
            result += int(s)
    return result


def test_bouns():
    assert add_string('2,1001') == 2


def test_lengthy():
    assert add_string('//***\n1***2***3') ==6
