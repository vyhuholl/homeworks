from flask import request
from flask import render_template
from pymystem3 import Mystem
import urllib.request

def download_page(pageUrl):
    try:
        page = urllib.request.urlopen(pageUrl)
        text = page.read().decode('utf-8')
        return text
    except:
        return('Error')

m = Mystem()

app = Flask(__name__)
