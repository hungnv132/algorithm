from basic_python.models import Person

list = [1 ,2, 3, 4, 5, 6, 7, 8]

print(list[4:2])

class Reverse(object):
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

if __name__ == '__main__':
    rev = Reverse('spam')
    # iter(rev)
    for char in rev:
        print(char)
