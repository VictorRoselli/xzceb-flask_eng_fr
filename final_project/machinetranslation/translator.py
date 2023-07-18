from deep_translator import MyMemoryTranslator


def englishToFrench(englishText):
    mytranslator = MyMemoryTranslator(source = 'en',target = 'fr')
    frenchText = mytranslator.translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    mytranslator = MyMemoryTranslator(source = 'fr',target = 'en')
    englishText = mytranslator.translate(frenchText)
    return englishText
