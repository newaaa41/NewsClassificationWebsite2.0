import pickle
from cleaner import stringClean
from translation import translate
import os

key = os.environ['google_api_key']


class classifier():

    def __init__(self, modelFile="model.bin", featuresFile="tfidf.bin"):
        with open(modelFile, "rb") as f:
            self.model = pickle.load(f)
        with open(featuresFile, "rb") as f:
            self.vect = pickle.load(f)
        self.lables = ['business', 'entertainment',
                       'politics', 'sport', 'tech']

    def classify(self, news=''):
        x = ' '.join([word for word in stringClean(news).split()])
        x, lang = translate(key, x)
        if(lang != 'en'):
            label = (" - ").join(self.lables)
            label = translate(key, label, lang)[0]
            labels = label.split("-")
        else:
            labels = self.lables

        X = self.vect.transform([x])
        prob = self.model.predict_proba(X)
        prob = list(prob[0])
        for i in range(len(prob)):
            prob[i] = round(prob[i]*100, 2)
        results = dict(zip(labels, prob))
        results = sorted(results.items(), key=lambda kv: (
            kv[1], kv[0]), reverse=True)

        return results
