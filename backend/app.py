from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/index')
@cross_origin()
def hello():
    return jsonify(message='Hello, World from flask backend!')

#if name == "main":
#    app.run(host="0.0.0.0", port="5000", debug=True)