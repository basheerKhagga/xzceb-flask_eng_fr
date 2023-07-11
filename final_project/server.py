from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation
app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    answer = machinetranslation.translator.english_to_french(textToTranslate)
    return "Translated text to French: " + answer

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    answer = machinetranslation.translator.french_to_english(textToTranslate)
    return "Translated text to English: " + answer

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
