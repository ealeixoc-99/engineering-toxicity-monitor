import toxicity
from detoxify import Detoxify

model = Detoxify('original')

def test_sentence_toxicity():
    sentence = 'I hate you'

    analyze = toxicity.sentence_toxicity_analysis(model, sentence)

    sentenceToxicity = analyze['toxicity'][0]

    assert sentenceToxicity > 0.9

def test_number_label():
    analyze = toxicity.sentence_toxicity_analysis(model, 'I love you')

    assert len(analyze) == 6