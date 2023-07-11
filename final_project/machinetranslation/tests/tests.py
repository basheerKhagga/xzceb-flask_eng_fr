import unittest

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test2(self):
        self.assertEqual(english_to_french('how are you'), 'im bien faire')


class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('im bien faire'), 'how are you')

    def test2(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hi')    

unittest.main()        