
def function_accept_any_number_of_arguments():
    """
    - Problem: You want to write a function that accepts any number of input
    arguments
    - Solution:
        - To accept any number of positional arguments, Use a * argument.
        - To accept any number of keyword arguments, use an argument that start
        with **.
        - * and ** argument only can appear as the last position argument.
    """

    def anyargs(*args, **kwargs):
        print(args)     # A tuple
        print(kwargs)   # A dict

    anyargs(1, 2, c=3, d=4)
    # (1, 2)
    # {'d': 4, 'c': 3}

    def avg(first, *rest):
        return (first + sum(rest)) / (1 + len(rest))

    print(avg(1, 2, 3))             # 2.0
    print(avg(1, 2, 3, 4, 5, 6))    # 3.5

    import html

    def make_element(name, value, **attrs):
        keyvals = [' %s="%s"' % item for item in attrs.items()]
        attr_str = ''.join(keyvals)
        element = '<{name}{attrs}>{value}</{name}>'.format(
            name=name,
            attrs=attr_str,
            value=html.escape(value)
        )
        return element

    e = make_element('item', 'Albatross', size='large', quantity=6)
    print(e)  # <item size="large" quantity="6">Albatross</item>

    e = make_element('p', '<spam>')
    print(e)  # <p>&lt;spam&gt;</p>


def function_only_accept_keyword_arguments():
    """
    - Problem: You want a function to only accept certain arguments by keyword.
    - Solution: place the keyword arguments after a * argument or single unnamed.
    """

    def recv(maxsize, *, block):
        print('do something')

    # recv(1024, True)  # TypeError: recv() takes 1 positional argument but 2 were given
    recv(1024, block=True)  # Ok



if __name__ == '__main__':
    function_only_accept_keyword_arguments()