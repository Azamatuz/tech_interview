# Change the Add method to handle new lines in the input format
def add_string(string):
    result = 0
    for s in string.replace('\n', '').split(','):
        if s.isdigit():
            result += int(s)
    return result


# custom test - just to try
def custom_test_two():
    if add_string('1\n,2,3') == 6 and add_string('') == 0:
        print("PASSED")
# uncomment blow to test
# custom_test_two()


# pytest
def test_two():
    assert add_string('1\n,2,3') == 6
    assert add_string('') == 0

