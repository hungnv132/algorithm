# Source: http://thecodeship.com/patterns/guide-to-python-function-decorators/
# Thank author so much!


def greet(name):
    return 'Hello, ' + name

# assign functions to variables
greet_somebody = greet

print(greet_somebody('John'))  # Hello, John


# ===============================
# Define function inside other functions
def greet2(name):
    def get_message():
        return "Hello"

    result = get_message() + ' ' + name
    return result

print(greet2('Hung'))       # Hello Hung


# ===============================
# Function can be passed as parameters to other functions
def greet3(name):
    return "Hello, " + name


def call_func(func):
    other_name = 'TTTT'
    return func(other_name)

print(call_func(greet2))        # Hello TTTT


# ===============================
# Functions can return other functions

def compose_greet_func():
    def get_message():
        return "Hello there!"

    return get_message

greet4 = compose_greet_func()
print(greet4())             # Hello there!


# ===============================
# Inner functin have access to the enclosing scope.
def compose_greet_func(name):
    def get_message():
        return "Hello there! " + name

    return get_message

greet4 = compose_greet_func('AAAA')
print(greet4())             # Hello there! AAAA


# ===============================
# Composition of Decorators
# Function decorators are simply wrappers to existing functions.
def get_text(name):
    return "I love {0}".format(name)


def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper

my_get_text = p_decorate(get_text)

print(my_get_text('Machine Learning'))  # <p>I love Machine Learning</p>


# with '@' keyword
@p_decorate
def get_text2(name):
    return "I like " + name

print(get_text2('BBBB'))  # <p>I like BBBB</p>


# =============================
# We wanted to decorate our get_text function by 2 other functions
def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper


def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper

get_text3 = div_decorate(p_decorate(strong_decorate(get_text)))
print(get_text3('This is content'))  # <div><p><strong>I love This is content</strong></p></div>


@div_decorate
@p_decorate
@strong_decorate
def get_text4(name):
    return "Welcome, " + name

print(get_text4('CCCCC'))   # <div><p><strong>Wellcome, CCCCC</strong></p></div>


# =============================
# Decorating Methods
def p_decorate(func):
    def func_wrapper(self):
        return "<p>{0}</p>".format(func(self))
    return func_wrapper


class Person(object):
    def __init__(self):
        self.name = "Hung"
        self.family = "Ng.vi"

    @p_decorate
    def get_fullname(self):
        return self.name + " " + self.family

my_person = Person()
print(my_person.get_fullname())  # <p>Hung Ng.vi</p>


# =================================
# putting *args and **kwargs as parameters for the wrapper
def p_decorate(func):
    def func_wrapper(*args, **kwargs):
        return "<p>{0}</p>".format(func(*args, **kwargs))
    return func_wrapper


class Person(object):
    def __init__(self):
        self.name = "Hung"
        self.family = "Nguyen Viet"

    @p_decorate
    def get_fullname(self, country="VN"):
        return self.name + " " + self.family + ", He's from " + country

my_person = Person()
print(my_person.get_fullname(country='Vietnam'))  # <p>Hung Nguyen Viet, He's from Vietnam</p>


# =================================
# Passing arguments to decorators
def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator


@tags("span")
def get_text5(name):
    return "Hello, " + name

print(get_text5("World"))  # <span>Hello, World</span>


# ==============================
# Debugging decorated functions

print(get_text5.__name__)  # Outputs func_wrapper, but expect to be get_text5

# The attributes __name__, __doc__, __module__ of get_text5 got overridden by those of the wrapper(func_wrapper)
# => Functools to the rescue

from functools import wraps


def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator


@tags("h1")
def get_text5(name):
    return "Hello, " + name

print(get_text5("World"))  # <h1>Hello, World</h1>
print(get_text5.__name__)  # Output: get_text5


# =============================================
# ID: 1234
# @property, @classmethod, @staticmethod

class Person(object):

    def __init__(self, first_name='Hung', last_name='Ng V.'):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def name(self):
        return self._first_name + ' ' + self._last_name

    @name.setter
    def name(self, value):
        name = value.split()
        self._first_name = name[0]
        self._last_name = name[1]

    @name.deleter
    def name(self):
        self._last_name = "Default"

    def __repr__(self):
        return self._first_name + ' ' + self._last_name


class Student(Person):

    def __init__(self, age=21, address='Hanoi', first_name='Hung', last_name='Ng V.'):
        self._age = age
        self._address = address
        super(Student, self).__init__(first_name, last_name)

    def __repr__(self):
        return "{0} {1}: {2} age".format(self._first_name, self._last_name,  self._age)

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def del_age(self):
        del self._age

    age = property(get_age, set_age,del_age)

    @classmethod
    def info(cls):
        return "Nguyễn Việt Hùng, 21 tuổi"

    @classmethod
    def display_info(cls, address):
        return "Information: %s, %s " % (cls.info(), address)

    @staticmethod
    def display_school():
        return "Hanoi University Science of Technology"

def demo_id_1234():
    person = Person();
    print(person.name)  # Output: Hung Nguyen V.

    person.name = 'Ronaldo Cr7'

    print(person.name)  # Output: Ronaldo Cr7
    del person.name

    print(person.name)   # Output: Ronaldo Default

    stu = Student()
    print(stu)          # Output: Hung Ng V.: 21 age

    print(stu.age)      # Output: 21
    stu.age = 24
    print(stu.age)      # Output: 24
    # del stu.age
    # print(stu.age)      # Output: Error: 'Student' object has no attribute '_age'

    print(Student.display_info("Hanoi"))    # Output: Information:Nguyễn Việt Hùng, 21 tuổi, Hanoi
    print(stu.display_info("Hanoi"))        # Output: Information:Nguyễn Việt Hùng, 21 tuổi, Hanoi
    print(Student.display_school())         # Output: Hanoi University Science of Technology
    print(stu.display_school())             # Output: Hanoi University Science of Technology


# =============================================
if __name__ == '__main__':
    demo_id_1234()
