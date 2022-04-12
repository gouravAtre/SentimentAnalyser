# -- coding: utf-8 --
'''
Created on 12-April-2022 23:33
Project: Sentiment Analyser 
@author: Gourav Atre
@email: gouravkumar1815@gmail.com
'''


class Group_Sentiment_Analyzer:
    config = 0

    def __init__(self, config):
        self.config = config

    @classmethod
    def find_sentiment(cls,config):
        # TrainedModel.predict(cls.config['input_data'])
        pass



if __name__ == "__main__":

    # for one object creation
    config = {"input_data":"Input data from whatsapp"}

    Group_Sentiment_Analyzer.find_sentiment(config)
