import unittest
from translator import english_to_french, french_to_english 

class TestFrenchtoEnglish (unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("NULL"),"NULL") #test that empty string returns empty string
        self.assertEqual(french_to_english("Bonjour"),"Hello") #test that Bonjour in French returns hello in english
 
 
class TestFrenchtoEnglish (unittest.TestCase):
    def test1(self):       
        self.assertEqual(english_to_french("NULL"),"NULL") #test that empty string returns empty string
        self.assertEqual(english_to_french("Hello"),"Bonjour") #test that Bonjour in French returns hello in english

unittest.main()