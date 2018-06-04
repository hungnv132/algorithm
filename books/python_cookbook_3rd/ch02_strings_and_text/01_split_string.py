import re


def split_string_on_any_of_multiple_delimiters():
    """
    - Problem: You need to split a string into fields, but the delimiters aren't
    consistent throughout the string.
    - Solution: re.split() method
    """
    line = 'asdf fjdk; afed, fjek,asdf,      foo'
    a = re.split(r'[;,\s]\s*', line)
    print(a)  # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

    fields = re.split(r'(;|,|\s)\s*', line)
    print(fields)
    # ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
    values = fields[::2]
    delimiters = fields[1::2] + ['']
    print(values)       # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
    print(delimiters)   # [' ', ';', ',', ',', ',', '']


if __name__ == '__main__':
    split_string_on_any_of_multiple_delimiters()