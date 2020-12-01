from madlib_cli import __version__
from madlib_cli.madlib_cli import read_template,parse,merge


def test_version():
    assert __version__ == '0.1.0'


data_string = '''I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}
{A First Name}'s {Adjective} sister and plan to steal her {Adjective}
{Plural Noun}!'''

data_to_change = ['Adjective', 'Adjective', 'A First Name', 'Past Tense Verb', 'A First Name', 'Adjective', 'Adjective', 'Plural Noun']

def test_read_template():
    actual = read_template('assets/file.txt')
    expected = data_string
    assert actual == expected

def test_parse():
    actual = parse(data_string)
    expected = data_to_change
    assert actual == expected

def test_merge():
    actual = merge([1,2,3,4,5,6,7,8])
    expected = """I the 1 and 2 3 have 4
5's 6 sister and plan to steal her 7
8!"""
    assert actual == expected
