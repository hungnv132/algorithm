def case_one():
    class A:

        def method(self):
            print("Class A")

    class B(object):

        def method(self):
            print("Class B")
            super(B, self).method()

    class C:

        def method(self):
            print("Class C")
            super(C, self).method()

    class D(C, B):

        def method(self):
            print("Class D")
            super(D, self).method()

    d = D()
    d.method()


if __name__ == '__main__':
    case_one()
