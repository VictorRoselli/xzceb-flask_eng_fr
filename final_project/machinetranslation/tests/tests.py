import unittest

from translator import englishToFrench
from translator import frenchToEnglish

class test_englishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench(englishText='Hello'),'Bonjour')
        self.assertEqual(englishToFrench(englishText='This is a test unit'),'Ceci est un test.')
        self.assertNotEqual(englishToFrench(englishText='Good night'),'Bonjour')

class test_englishToFrench(unittest.TestCase):
    def test2(self):
        self.assertEqual(frenchToEnglish(frenchText='Ceci est un test'),'test the board')
        self.assertEqual(frenchToEnglish(frenchText='Bonjour'),'Hello')
        self.assertNotEqual(frenchToEnglish(frenchText='je veux de glaçons'),'I want ice cream')

unittest.main()