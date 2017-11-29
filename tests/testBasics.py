import sys
sys.path.append("..")
from unittest.mock import patch
import unittest
import basics


class MultiplyTest(unittest.TestCase):

    def setUp(self):
        self.test_elem = (([0, 1, 2], 0), ([1, 3, 10, 20], 600), ([10, 100, 1000], 1000000))

    def testCalculation(self):
        for (i, val) in self.test_elem:
            self.assertEqual(basics.multiply(i), val)

    def tearDown(self):
        self.test_elem = None


class ReverseTest(unittest.TestCase):

    def setUp(self):
        self.check_elem = (("", ""), ("mike", "ekim"), ("poisen! .ua", "au. !nesiop"))

    def testFunction(self):
        for i, val in self.check_elem:
            self.assertEqual(basics.my_reverse(i), val)

    def tearDown(self):
        self.check_elem = None


class PalindromeTest(unittest.TestCase):

    def setUp(self):
        self.check_true = ("ror", "a but tuba", "a man, a plan, a canal: Panama")
        self.check_false = ("truth", "Be or not to be?", "Developer")

    def testFunction(self):
        for i in self.check_true:
            self.assertTrue(basics.is_palindrome(i))

        for j in self.check_false:
            self.assertFalse(basics.is_palindrome(j))

    def tearDown(self):
        self.check_true = None
        self.check_false = None


class CipherTest(unittest.TestCase):

    def setUp(self):
        self.check_elem = (("Scorpion", 2, "Ueqtrkqp"),
                           ("Dear Guest, welcome!", 26, "Dear Guest, welcome!"),
                           ("/5~y  @", 123123, "/5~l  @"))

    def testFunction(self):
        for (i, j, val) in self.check_elem:
            self.assertEqual(basics.caesar_cipher(i, j), val)

    def tearDown(self):
        self.check_elem = None


@patch('random.randint')
class GameTest(unittest.TestCase):

    def testFunction(self, mocked_randint):
        mocked_randint.return_value = 21
        self.assertEqual(basics.game(1, 123), 21)


class BracketsTest(unittest.TestCase):
    def setUp(self):
        self.test_elem = (("[[[[]]]]", "OK"), ("[[[]]]]]]]]", "NOT OK"), ("[", "NOT OK"))

    def testCalculation(self):
        for (i, val) in self.test_elem:
            self.assertEqual(basics.checkBrackets(i), val)

    def tearDown(self):
        self.test_elem = None


class Char_freqTest(unittest.TestCase):
    def setUp(self):
        self.test_elem = (("abbwkd", {'a': 1, 'b': 2, 'w': 1, 'k': 1, 'd': 1}),
                          ("mvc", {'m': 1, 'v': 1, 'c': 1}),
                          ("Ron!!", {'R': 1, 'o': 1, 'n': 1, '!': 2}))

    def testCalculation(self):
        for (i, val) in self.test_elem:
            self.assertDictEqual(basics.char_freq(i), val)

    def tearDown(self):
        self.test_elem = None


class Dec_to_binTest(unittest.TestCase):
    def setUp(self):
        self.check_elem = ((0, 0), (2, 10), (50, 110010), (99, 1100011))

    def testFunction(self):
        for i, val in self.check_elem:
            self.assertEqual(basics.dec_to_bin(i), val)

    def tearDown(self):
        self.check_elem = None


if __name__ == "__main__":
    unittest.main()
