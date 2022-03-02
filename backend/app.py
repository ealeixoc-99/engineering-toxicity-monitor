from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from detoxify import Detoxify
import toxicity

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

model = Detoxify('original')

@app.route('/index', methods=['GET'])
@cross_origin()
def hello():
    sentenceToAnalyze = request.args.get('sentence')
    analyze = toxicity.sentence_toxicity_analysis(model, sentenceToAnalyze)
    return jsonify(message=analyze)
