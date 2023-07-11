''' Code for translation of strings '''

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    ''' Translates a string in english to French'''
    french_text = MyMemoryTranslator(source="en-US", target="french").translate(text= english_text)
    return french_text


def french_to_english(french_text):
    ''' Translates a string in French to english'''
    english_text = MyMemoryTranslator(source="french", target="en-US").translate(text= french_text)
    return english_text
