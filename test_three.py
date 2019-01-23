# Support a custom delimiter
custom_delimiter = '$'
simple_str = '//,\n1,2,3'


def add_string(string, delimiter):
    result = 0
    if len(string) != 0:
        string = ''.join(simple_str.replace(',', custom_delimiter).splitlines())
        for s in string:
            if s.isdigit():
                result += int(s)
    return result


# custom test - just to try
def custom_test_three():
    if add_string('//,\n1,2,3', custom_delimiter) == 6 and add_string('', custom_delimiter) == 0:
        print("PASSED")
# uncomment blow to test
# custom_test_three()


def test_three():
    assert add_string('//,\n1,2,3', custom_delimiter) == 6


def test_three_zero():
    assert add_string('', custom_delimiter) == 0
