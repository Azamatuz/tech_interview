# Support a custom delimiter
import warnings
custom_delimiter = '$'
simple_str = '//,\n1,-2,3'


def add_string(string, delimiter):
    result = 0
    negative_gigits = []
    if len(string) != 0:
        string = ''.join(simple_str.replace(',', delimiter).splitlines())
        string = string.split(delimiter)
        for s in string:
            if s.lstrip('-').isdigit():
                if int(s) >= 0:
                    result += int(s)
                else:
                    negative_gigits.append(int(s))
                    warnings.warn('Negatives not allowed')

        #
        warnings.warn('{} {}'.format('Negative numbers:', negative_gigits))

    return result


# custom test - just to try
def custom_test_four():
    if add_string('//,\n1,-2,3', custom_delimiter) == 4 and add_string('', custom_delimiter) == 0:
        print("PASSED")
# uncomment blow to test
# custom_test_four()


def test_four():
    assert add_string('//,\n1,-2,3', custom_delimiter) == 4


def test_four_zero():
    assert add_string('', custom_delimiter) == 0
