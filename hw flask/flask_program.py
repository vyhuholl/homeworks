from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('127.0.0.1/')
@app.route('127.0.0.1/<name>')
def main_page(name=None):
    return render_template('main_page.html', name=name)

@app.route('127.0.0.1/stats')
def stats():
    native_language = request.args['native_language']
    dictionary = {}
    for i in native_language:
        if i not in dictionary:
            dictionary[i] = native_language.count(i)
    return render_template('stats.html', name=name)

@app.route('127.0.0.1/json')
def json():
    sharp_knife = json.dumps(request.args['sharp_knife'])
    sharp_sword = json.dumps(request.args['sharp_sword'])
    sharp_nail = json.dumps(request.args['sharp_nail'])
    sharp_saber = json.dumps(request.args['sharp_saber'])
    sharp_blade = json.dumps(request.args['sharp_blade'])
    sharp_scythe = json.dumps(request.args['sharp_scythe'])
    sharp_scissors = json.dumps(request.args['sharp_scissors'])
    sharp_needle = json.dumps(request.args['sharp_needle'])
    sharp_arrow = json.dumps(request.args['sharp_arrow'])
    sharp_stake = json.dumps(request.args['sharp_stake'])
    return render_template('json.html', name=name)

@app.route('127.0.0.1/search')
def search():
    return render_template('search.html', name=name)

@app.route('127.0.0.1/results')
def results():
    result = request.args['search']
    results_list = {}
    return render_template('results.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
