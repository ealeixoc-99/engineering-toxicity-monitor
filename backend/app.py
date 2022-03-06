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
import psutil

UPDATE_PERIOD = 300

REQUESTS = Counter('total_request', 'User requests count')
SYSTEM = Gauge('system_usage', 'Hold current system resource usage',['resource_type'])
LATENCY = Histogram('Latency', 'Time spent processing request', buckets=[0.0001, 0.0002, 0.0005, 0.001, 0.01, 0.1])# Hardware metrics

SYSTEM.labels('CPU').set(psutil.cpu_percent())
SYSTEM.labels('Memory').set(psutil.virtual_memory()[2])
SYSTEM.labels('Disk Usage').set(psutil.disk_usage(psutil.disk_partitions()[0].mountpoint)[2])

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
model = Detoxify('original')

@app.route('/index', methods=['GET'])
@cross_origin()
def hello():
    start = time.time()
    # Software metrics
    # User request count
    REQUESTS.inc()
    # Request time metric
    LATENCY.observe(time.time() - start)
    SYSTEM.labels('CPU').set(psutil.cpu_percent())
    SYSTEM.labels('Memory').set(psutil.virtual_memory()[2])
    SYSTEM.labels('Disk Usage').set(psutil.disk_usage(psutil.disk_partitions()[0].mountpoint)[2])
    # Response for the back
    sentenceToAnalyze = request.args.get('sentence')
    analyze = toxicity.sentence_toxicity_analysis(model, sentenceToAnalyze)
    return jsonify(message=analyze)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8010)
    app.run(host='0.0.0.0', port=5000)
