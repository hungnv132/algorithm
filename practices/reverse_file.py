from data_structures.stack import Stack


def reverse_file(file_name):
    S = Stack()
    original = open(file_name)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()

    output = open(file_name, 'w')  # reopen and overwrite the contents
    while not S.is_empty():
        output.write(S.pop()+ '\n')
    output.close()


if __name__ == '__main__':
    reverse_file('text.txt')