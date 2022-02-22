from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import toxicity

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/index')
@cross_origin()
def hello():
    analyze = toxicity.sentence_toxicity_analysis("answerToPredict")
    return jsonify(message=analyze)