#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 16:11:27 2018

@author: anamika
"""

from util import read_data, naive_bayes_learner, naive_bayes_classifier
from sklearn.model_selection import train_test_split
import numpy as np

def main():
    filename = "data/data.csv"
    column_type = {'Review Text':str, 'Sentiment':str, 'Fit':str, 'Fabric':str, 'Color':str, 'Style':str, 'Cost':str}
    x_label = 'Review Text'
    y_label_sentiment = 'Sentiment'
    sentiment_labels = ['-1', '0', '1']
    data = read_data(filename, column_type, x_label=x_label, y_label=y_label_sentiment, clean_data=True)
    x = data[x_label]
    y = data.drop([x_label], axis=1)

    ## split data : train and test
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=50)

    # naive bayes

    w_prob, c_prob = naive_bayes_learner(X_train, y_train[y_label_sentiment], sentiment_labels, verbose=False)

    expected_class_list = np.zeros(len(y_test))
    predicted_class_list = np.zeros((len(y_test)))
    for index, (data, expected_class) in enumerate(zip(X_test, y_test[y_label_sentiment])):
        predicted_class, log_prob = naive_bayes_classifier(w_prob, c_prob, sentiment_labels, data)
        expected_class_list[index] = expected_class
        predicted_class_list[index] = predicted_class
        # print predicted_class, expected_class

    print "Total: ", len(expected_class_list)
    print "True positives: ", np.sum(expected_class_list == predicted_class_list)
    print "Accuracy: ", np.mean(expected_class_list == predicted_class_list)


if __name__ == '__main__':
    main()