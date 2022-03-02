def sentence_toxicity_analysis(model, answerToPredict):
    """ This function will prepare the sentence and then apply the detoxify model to determine the toxicity
    of sentence.

    String answerToPredict : sentence to predict

    return String : the prediction
    """

    results = model.predict([answerToPredict])

    return results
