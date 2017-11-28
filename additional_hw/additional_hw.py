from flask import request
from flask import render_template
from pymystem3 import Mystem

m = Mystem()

app = Flask(__name__)
