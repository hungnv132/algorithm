from data_structures.stack import Stack


def is_matched_html(html_text):

    stack = Stack()
    i = html_text.find('<')

    while i != -1:
        j = html_text.find('>', i)
        tag_name = html_text[i + 1: j]
        # if html_text[i+1] != '/':
        if not tag_name.startswith('/'):  # opening tag or closing tag
            print(tag_name)
            stack.push(tag_name)
        else:
            if stack.is_empty():
                return False
            # tag_name = html_text[i + 2: j]
            if tag_name[1:] != stack.pop():
                return False
        i = html_text.find('<', j)

    return stack.is_empty()


if __name__ == '__main__':
    s = ' <ul><li>Vietnam</li><li>USA</li><li>Japan</li></ul><h1></h1>'
    print(is_matched_html(s))
    # print(s.find('n3',2))
    # i = s.find('<')
    # while i != -1:
    #     j = s.find('>', i)
    #     print(j)
    #     print (s[i+1:j].strip())
    #     i = s.find('<', j)