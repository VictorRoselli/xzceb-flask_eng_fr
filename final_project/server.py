'''
This module handles the server and html
'''

from machinetranslation import translator
from flask import Flask, render_template, request
import json
from deep_translator import MyMemoryTranslator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    '''
    Connects the end point to english to french function
    '''
    text_to_translate = request.args.get('textToTranslate')
    my_translator = MyMemoryTranslator(source = 'en',target = 'fr')
    french_text = my_translator.translate(text_to_translate)
    return french_text

@app.route("/frenchToEnglish")
def french_to_english():
    '''
    Connects the end point to french to english function
    '''
    text_to_translate = request.args.get('textToTranslate')
    my_translator = MyMemoryTranslator(source = 'fr',target = 'en')
    english_text = my_translator.translate(text_to_translate)
    return english_text


@app.route("/")
def render_index_page():
    '''
    Renders the page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)




