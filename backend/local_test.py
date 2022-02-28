import toxicity

def test_sentence_toxicity():
    sentence = 'I hate you'

    analyze = toxicity.sentence_toxicity_analysis(sentence)

    sentenceToxicity = analyze['toxicity'][0]

    assert sentenceToxicity > 0.9

def test_number_label():
    analyze = toxicity.sentence_toxicity_analysis('I love you')

    assert len(analyze) == 6