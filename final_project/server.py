from machinetranslation import translator
from flask import Flask, render_template, request
import json
from deep_translator import MyMemoryTranslator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    mytranslator = MyMemoryTranslator(source = 'en',target = 'fr')
    frenchText = mytranslator.translate(textToTranslate)
    return frenchText

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    mytranslator = MyMemoryTranslator(source = 'fr',target = 'en')
    englishText = mytranslator.translate(textToTranslate)
    return englishText



@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
