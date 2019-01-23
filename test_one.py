# Create a simple String calculator with a method: int Add(string numbers)
def add_string(string):
    result = 0
    if len(string.strip()) != 0:
        for s in string.split(','):
            result += int(s)
    return result


def test_answer_one():
    assert add_string('1, 2, 5') == 8
    assert add_string('') == 0
