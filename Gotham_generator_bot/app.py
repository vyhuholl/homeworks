import conf
import flask
import telebot
import pickle
from random import uniform

def unirand(seq):
    sum_, freq_ = 0, 0
    for item, freq in seq:
        sum_ += freq
    rnd = uniform(0, sum_)
    for token, freq in seq:
        freq_ += freq
        if rnd < freq_:
            return token

def generate_sentence(model):
    phrase = ''
    t0, t1 = '$', '$'
    while 1:
        t0, t1 = t1, unirand(model[t0, t1])
        if t1.endswith('$'): break
        if t1.endswith('.') or t1.endswith('?') or t1.endswith('!') or t0.endswith('$'):
            phrase += t1
        else:
            phrase += ' ' + t1
    phrase = phrase.strip(' ')
    return phrase.capitalize()

def unpickle_file(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

model = unpickle_file('markov_model')


bot = telebot.TeleBot(conf.TOKEN, threaded = False)

bot.remove_webhook()
bot.set_webhook(url="https://gothamgenerator.herokuapp.com/bot")

app = flask.Flask(__name__)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello, delicious friend. Say something.")

@bot.message_handler(func=lambda m: True)
def send_len(message):
    reply = generate_sentence(model)
    bot.send_message(message.chat.id, reply)

@app.route("/bot", methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)
    
if __name__ == '__main__':
    import os
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
