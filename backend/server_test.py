import requests

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
