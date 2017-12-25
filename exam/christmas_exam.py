import re
import json
from flask import Flask
from flask import request
from flask import render_template

dictionary = {}
dictionary_reversed = {}

regFindWord = re.compile('<tr>(.*?)</tr>', flags= re.DOTALL)
regTag = re.compile('<.*?>', flags= re.DOTALL)

for i in range(187, 207):
    for j in range(100):
        try:
            with open(str(i) + '.' + str(j) + '.html') as html:
                html = html.read()
                words = regFindWord.findall(html)
                for word in words:
                    word = regTag.sub('_', word)
                    word = word.split('_')
                    thai_word = word[0]
                    english_word = word[-1]
                    pos = word[-2]
                    if pos != 'example sentence':
                        dictionary[thai_word] = english_word.split('; ')
                        if english_word in dictionary_reversed:
                            (dictionary_reversed[english_word]).append(thai_word)
                        else:
                            dictionary_reversed[english_word] = [thai_word]
                html.close()
        except:
            continue

f = open('dictionary.json', 'w', encoding = 'utf-8')
json.dump(dictionary, f)
f.close()

f1 = open('dictionary_reversed.json', 'w', encoding = 'utf-8')
json.dump(dictionary_reversed, f1)
f1.close()

app = Flask(__name__)

@app.route('127.0.0.1/')

@app.route('127.0.0.1/<name>')
def main_page(name=None):
    return render_template('main_page.html', name=name)

@app.route('127.0.0.1/result')
def result_page(name = None):
    if request.args:
        english_word = request_args('word')
        if english_word in dictionary_reversed:
            ans = (dictionary_reversed[english_word]).join('; ')
        else:
            ans = 'Ничего не нашлось!'
    return render_template('result_page.html', new_word=ans)

if __name__ == '__main__':
   app.run(debug=True)
