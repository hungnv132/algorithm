import unittest


class TestStringMethod(unittest.TestCase):

    def test_uppper(self):
        self.assertEqual('hung'.upper(), 'HUNG')

    def test_isupper(self):
        self.assertTrue('HUNG'.isupper())
        self.assertFalse('Hung'.isupper())

    def test_split(self):
        s = 'Hello World'
        self.assertTrue(s.split(), ['Hello', 'World'])

        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(8)


# RUN: python -m unittest -v basic_examples
# or
if __name__ == '__main__':
    unittest.main()
