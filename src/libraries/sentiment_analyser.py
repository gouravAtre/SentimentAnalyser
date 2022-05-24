import pickle
from sklearn.feature_extraction.text import CountVectorizer

class GroupSentimentAnalyser():

    @classmethod
    def find_sentiment(cls,data):
        # try:
        count_vectorizer = CountVectorizer(ngram_range=(1,2))    # Unigram and Bigram
        final_vectorized_data = count_vectorizer.fit_transform([data])  
        model_filename = "src/data/model/sentiment_naive.sav"

        model = pickle.load(open(model_filename, 'rb')) # the model will be read into the object my_knn_model 
                                                            # and you can use the same model to predict the new data.

        result = model.predict(final_vectorized_data) # X_test is where the new data that is to be predicted is inserted, 
                                            # here X_test is a part of dataset 
        # except Exception as e:
        #     return "Code fat gya :: At Sentiment Analyser"

        if result:
            return result
        return "Not detected"