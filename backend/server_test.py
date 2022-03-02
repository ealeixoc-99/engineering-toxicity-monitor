import requests
import time

def test_get_index_status_code():
    sentence = "sentence='I hate you'"
    url = 'http://127.0.0.1:5000/index?' + sentence

    response = requests.get(url)

    assert response.status_code == 200

def test_get_index_toxicity():
    sentence = "sentence='I hate you'"
    url = 'http://127.0.0.1:5000/index?' + sentence

    response = requests.get(url)

    data = response.json()

    sentenceToxicity = data['message']['toxicity'][0]

    assert sentenceToxicity > 0.9

def test_stress_handle_100_requests_per_minute():
    sentence = "sentence='I hate you'"
    url = 'http://127.0.0.1:5000/index?' + sentence

    start_time = time.time()
    for i in range(100):
        response = requests.get(url)
        total_time = time.time() - start_time
        assert total_time < 60, "Error !"
        print("Time : " + str(total_time) + " for " + str(i+1) + " requests")