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
    return render_template('stats.html', name=name)

@app.route('127.0.0.1/json')
def json():
    return render_template('json.html', name=name)

@app.route('127.0.0.1/search')
def search():
    return render_template('search.html', name=name)

@app.route('127.0.0.1/results')
def results():
    results_list = {}
    return render_template('results.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
