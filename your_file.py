import unittest


def my_special_function(num):
    return num


class TestSomething(unittest.TestCase):

    def test_something(self):
        self.assertEqual(my_special_function(1), 1)
        

        
