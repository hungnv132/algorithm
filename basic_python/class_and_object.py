from basic_python.models import Person

if __name__ == '__main__':
    one_man = Person
    print('class Person: ' + str(Person))  # <class 'basic_python.models.Person'>
    print('class Person().__class__: ' + str(Person().__class__))  # <class 'basic_python.models.Person'>
    print('class \'one_man\': ' + str(one_man))  # <class 'basic_python.models.Person'>
    print('object Person(): ' + str(Person()))  # hungnv132 - age 24
    print('object one_man(): ' + str(one_man()))  # hungnv132 - age 24

    person =  Person()
    student = Person()
    student.set_name('hnv132')

    show_name = person.get_name  # assign a method object reference
    print(person.get_name())  # hungnv132
    print(show_name())  # hungnv132
    print(student.get_name())  # hnv132
    a = 1
    print()
    print(int)
    print(person.m())




