import zmq
from flask import Flask, render_template, request, jsonify, g
import lang
import config

app = Flask(__name__)

@app.before_request
def before_request():
    context = zmq.Context()
    g.socket = context.socket(zmq.REQ)
    g.socket.connect('tcp://%s:%d' % (config.tserver_host, config.tserver_port))

def translator(sentence):
    g.socket.send(sentence.encode('utf8'))
    return g.socket.recv().decode('utf8')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate')
def translate():
    inp = request.args.get('input', '')
    sentences = map(lang.preprocess, lang.sent_tokenize(inp))
    translations = map(translator, sentences)
    out = map(lang.postprocess, translations)
    return jsonify(output = '<br/>'.join(out))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
