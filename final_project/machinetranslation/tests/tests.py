import unittest
from translator import english_to_french, french_to_english #pylint: disable=E0401

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test2(self):
        self.assertNotEqual(english_to_french('how are you'), 'im bie faire')


class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(french_to_english('im bie faire'), 'how are you')

    def test2(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hi')    

unittest.main()        