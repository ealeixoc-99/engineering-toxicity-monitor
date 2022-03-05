from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from detoxify import Detoxify
import toxicity
from prometheus_client import start_http_server
from prometheus_client import Counter
from prometheus_client import Gauge
from prometheus_client import Summary
from prometheus_client import Histogram
import time

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
REQUESTS = Counter('hello_worlds_total', 'Hello Worlds requested')
EXCEPTIONS = Counter('hello_world_exceptions_total', 'Exceptions serving Hello World.')
INPROGRESS = Gauge('hello_worlds_inprogress', 'Number of Hello Worlds in progress.')
LAST = Gauge('hello_world_last_time_seconds', 'The last time a Hello World was served.')
LATENCY = Histogram('Latency', 'Time for a request Hello World.', buckets=[0.0001, 0.0002, 0.0005, 0.001, 0.01, 0.1])

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    time.sleep(t)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
model = Detoxify('original')

@app.route('/index', methods=['GET'])
@cross_origin()
def hello():
    start = time.time()
    REQUESTS.inc()
    INPROGRESS.inc()
    LAST.set(time.time())
    INPROGRESS.dec()
    LATENCY.observe(time.time() - start)
    sentenceToAnalyze = request.args.get('sentence')
    analyze = toxicity.sentence_toxicity_analysis(model, sentenceToAnalyze)
    return jsonify(message=analyze)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8010)
    app.run(host='0.0.0.0', port=5000)
    # Generate some requests.
    while True:
        process_request(1)


