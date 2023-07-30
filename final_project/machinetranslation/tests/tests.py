import unittest
from machinetranslation import translator

from translator import english_to_french
from translator import french_to_english

class test_english_to_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(english_text='Hello'),'Bonjour')
        self.assertEqual(english_to_french(english_text='This is a test unit'),'Ceci est un test.')
        self.assertNotEqual(english_to_french(english_text='Good night'),'Bonjour')

class test_french_to_english(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english(frenchText='Ceci est un test'),'test the board')
        self.assertEqual(french_to_english(frenchText='Bonjour'),'Hello')
        self.assertNotEqual(french_to_english(frenchText='je veux de glaçons'),'I want ice cream')

unittest.main()