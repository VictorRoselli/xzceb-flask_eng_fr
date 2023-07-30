'''
This module handles the various language translations

'''

from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    '''
    Translates from english to french
    '''
    my_translator = MyMemoryTranslator(source = 'en-GB',target = 'fr-FR')
    french_text = my_translator.translate(english_text)
    return french_text


def french_to_english(french_text):
    '''
    Translates from french to english
    '''
    my_translator = MyMemoryTranslator(source = 'fr-FR',target = 'en-GB')
    english_text = my_translator.translate(french_text)
    return english_text
