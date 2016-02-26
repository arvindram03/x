from flask import Flask
from flask import request
app = Flask(__name__, static_url_path='/static')
import nltk
import json

@app.route('/process')
def try_to_make_sense():
	sentence = request.args.get('q')
	words = nltk.tokenize.word_tokenize(sentence) 
	return json.dumps(nltk.pos_tag(words))

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)