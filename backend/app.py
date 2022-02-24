from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import toxicity

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/index', methods=['GET'])
@cross_origin()
def hello():
    sentenceToAnalyze = request.args.get('sentence')
    analyze = toxicity.sentence_toxicity_analysis(sentenceToAnalyze)
    return jsonify(message=analyze)
