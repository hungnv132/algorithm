
def matching_text_at_the_start_or_end_of_string():
    """
    - Problem: You need to check the start or end of a strng for specific text
    patterns, such as filename extensions, URL schemas,...
    - Solution: str.startswith() or str.endswith()
    """
    filename = 'spam.txt'
    b = filename.endswith('.txt')
    print(b)    # True
    b = filename.startswith('file:')
    print(b)    # False
    url = 'http://www.python.org'
    b = url.startswith('http')
    print(b)    # True

    # If you need to check against multiple choices, provide a tuple of
    # possibilities ot startswith() or endswith()
    filenames = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
    c = [name for name in filenames if name.endswith(('.c', '.h'))]
    print(c)  # ['foo.c', 'spam.c', 'spam.h']
    b = any(name.endswith('.py') for name in filenames)
    print(b)   # True


def matching_strings_using_shell_wildcard_patterns():
    """
    - Problem: You want to match text using the same wildcard patterns as are
    commonly used when working in Unix shells (*.py, Dat[0-9]*.csv, ...)
    - Solution: The `fnmatch` module provides 2 functions fnmatch() and
    fnmatchcase()
    """
    from fnmatch import fnmatch, fnmatchcase
    filename = 'foo.txt'
    b = fnmatch(filename, '*.txt')
    print(b)  # True
    b = fnmatch(filename, '?oo.txt')
    print(b)  # True

    # NEXT
    b = fnmatch('Dat45.csv', 'Dat[0-9]*')
    print(b)  # True
    names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
    c = [name for name in names if fnmatch(name, 'Dat*.csv')]
    print(c)  # ['Dat1.csv', 'Dat2.csv']

    # NEXT
    addresses = [
        '5412 N CLARK ST',
        '1060 W ADDISON ST',
        '1039 W GRANVILLE AVE',
        '2122 N CLARK ST',
        '4802 N BROADWAY',
    ]
    c = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
    print(c)  # ['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']
    c = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
    print(c)  # ['5412 N CLARK ST']


def matching_and_searching_for_text_patterns():
    """
    - Problem: You want to match or search text for a specific pattern.
    - Solution: str.find(), str.startswith(), str.endswith()
    For more complicated matching, use regular expression and the `re` module.
    """
    import re

    text = 'yeah, but no, but yeah, but no, but yeah'
    print(text.find('no'))  # 10

    # NEXT
    text1 = '11/27/2012'
    text2 = 'Nov 27, 2012'
    if re.match(r'\d+/\d+/\d+', text1):
        print('yes')
    else:
        print('no')
    # Yes

    if re.match(r'\d+/\d+/\d+', text2):
        print('yes')
    else:
        print('no')
    # no

    # if to perform a lot of matches using the same patter, it usually pays to
    # recompile the regular expresion pattern into a pattern object first.
    date_pattern = re.compile(r'\d+/\d+/\d+')
    if date_pattern.match(text1):
        print('yes')
    else:
        print('no')
    # Yes

    if date_pattern.match(text2):
        print('yes')
    else:
        print('no')
    # no

    # NEXT: search text use the findall()
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    c = date_pattern.findall(text)
    print(c)  # ['11/27/2012', '3/13/2013']

    # When defining regular expression, you can capture groups by enclosing
    # parts of the pattern in parentheses
    date_pattern = re.compile(r'(\d+)/(\d+)/(\d+)')
    m = date_pattern.match('08/08/2016')
    print(m.group(0))  # 08/08/2016
    print(m.group(1))  # 08
    print(m.group(2))  # 08
    print(m.group(3))  # 2018
    print(m.groups())  # ('08', '08', '2016')

    day, month, year = m.groups()
    print(day, month, year)  # 08 08 2016

    # NEXT: findall() splits into tuples
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    c = date_pattern.findall(text)
    print(c)  # [('11', '27', '2012'), ('3', '13', '2013')]

    # NEXT: finditer()
    for m in date_pattern.finditer(text):
        print(m.groups())
        # ('11', '27', '2012')
        # ('3', '13', '2013')


if __name__ == '__main__':
    matching_and_searching_for_text_patterns()