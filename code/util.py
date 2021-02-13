import pandas as pd
from nltk.tokenize import word_tokenize
from math import log
from collections import defaultdict
from numpy import argmax
from string import punctuation
import re
import string
from nltk.stem import PorterStemmer

###
# loading all lexicons
###
# emoticons = {}
# with open("data/lexicons/emoticons.txt", 'r') as f:
#     for line in f:
#         k, v = re.split(r'\t+', line.rstrip('\t\n'))
#         emoticons[k] = v
#
# prioritized_shortened = {"can't" : "can not", "ain't": "are not"}
# shortened = {}
# with open("data/lexicons/'.txt", 'r') as f:
#     for line in f:
#         k, v = re.split(r'\t+', line.rstrip('\t\n'))
#         shortened[k] =  v
#
# slang = {}
# with open("data/lexicons/slang.txt", 'r') as f:
#     for line in f:
#         k, v = re.split(r'\t+', line.rstrip('\t\n'))
#         slang[k] = v
#
# american_to_british = {}
# with open("data/lexicons/british_to_american_spelling.txt", 'r') as f:
#     for line in f:
#         k, v = re.split(r'\t+', line.rstrip('\t\n'))
#         american_to_british[k] = v


trans = string.maketrans(string.punctuation, " "*len(string.punctuation))


def clean_words(word, cleaners):
    for cleaner_name, cleaner_dict in cleaners.iteritems():
        if word in cleaner_dict:
            word = cleaner_dict[word]
    return word


def clean(string_data, prior_to_punc, post_punc):
    porter = PorterStemmer()
    words = string_data.lower().split(' ')
    clean_data = []
    for word in words:
        word = clean_words(word, prior_to_punc)
        # word = word.translate(trans)
        word = re.sub('[^A-Za-z0-9]', ' ', word)
        word = clean_words(word, post_punc)
        word = porter.stem(word)
        clean_data.append(word)
    return " ".join(clean_data)


def read_file(filename):
    m = {}
    with open(filename) as f:
        for line in f:
            k, v = re.split(r'\t+', line.rstrip('\t\n'))
            m[k] = v
    return m


def load_cleaners(cleaners_map):
    cleaners = defaultdict(dict)
    for k, v in cleaners_map.iteritems():
        for cleaner, filename in v.iteritems():
            cleaners[k][cleaner] = read_file(filename)
    return cleaners['prior_to_punc'], cleaners['post_punc']


def data_cleaner(data, x_label, y_label, verbose=False):
    # drop rows with NaN
    data = data.dropna(how='any', subset=[x_label, y_label])
    cleaners = {
        'prior_to_punc': {
            'emoticons': 'data/lexicons/emoticons.txt',
            'shortened': 'data/lexicons/shortened.txt'
        }, 'post_punc': {
            'slang': 'data/lexicons/slang.txt',
            'british_to_american': 'data/lexicons/british_to_american_spelling.txt'
        }
    }
    prior_to_punc, post_punc = load_cleaners(cleaners)
    # replace all lexicons, remove punctuation
    i = 0
    for index, row in data.iterrows():
        if verbose:
            print row[x_label]

        # replace slang
        # for k, v in slang.iteritems():
        #     row[x_label] = row[x_label].replace(" "+k+" ", " "+v+" ")
        # replace emoticons
        # for k, v in emoticons.iteritems():
        #     row[x_label] = row[x_label].replace(k, v)
        # # replace short forms like I'll, can't, isn't, etc.
        # for k, v in shortened.iteritems():
        #     row[x_label] = row[x_label].replace("can't", "can not").replace(k, " " + v)

        # replace slang and then British spellings to English spellings
        if i < 20:
            print row[x_label]
        row[x_label] = clean(row[x_label], prior_to_punc, post_punc)
        if i < 20:
            print row[x_label]
            print ""
            i += 1
        #     if word in slang:
        #         row[x_label] = row[x_label].replace(" " + k + " ", " " + v + " ")
        #     if word in american_to_british:
        #         row[x_label] = row[x_label].replace(word, american_to_british[word])
        #
        # row[x_label] = row[x_label].translate(None, punctuation).lower()
        if verbose:
            print row[x_label]
            print "---------------"

    if verbose:
        print "cleaning Done"

    return data


def read_data(filename, column_type, x_label, y_label, clean_data=True):
    data = pd.read_csv(filename, dtype=column_type)

    ## assert data


    ## data cleaning
    if clean_data:
        return data_cleaner(data, x_label, y_label)
    return data


def get_word_count(train_data):

    word_count = defaultdict(int)
    for review in train_data:
        for word in word_tokenize(review):
            word_count[word] += 1
    return word_count


def get_unknown_words(train_data, threshold = 1):
    word_count = get_word_count(train_data)
    words_to_remove = set()

    for (k, v) in word_count.iteritems():
        if v <= threshold:
            words_to_remove.add(k)

    # for word in words_to_remove:
    #     del word_count[word]
    # word_count['<unk>'] = unk_count
    return words_to_remove


reverse_class_labels = {}
unknown_label = '<unk>'


###
# expected usage:
# naive_bayes_learner(train_data, ['-1', '0', '1'], 'Review Text', 'Sentiment')
###
def naive_bayes_learner(X, y, class_labels, verbose=False):
    global reverse_class_labels, unknown_label
    w_scores = {}
    c_scores = [0] * len(class_labels)
    class_label_map = dict((class_label, index) for index, class_label in enumerate(class_labels))
    reverse_class_labels = dict((index, class_label) for index, class_label in enumerate(class_labels))
    unknown_words = get_unknown_words(X)

    for index, (x, y) in enumerate(zip(X, y)):
        current_class = class_label_map[y]
        c_scores[current_class] += 1
        for word in word_tokenize(x):
            if word in unknown_words:
                word = unknown_label
            if word not in w_scores:
                w_scores[word] = [0] * len(class_labels)
            w_scores[word][current_class] += 1

    if verbose:
        print "Class scores: ", c_scores

    # convert int to float
    c_scores = [float(score) for score in c_scores]

    for k, v in w_scores.iteritems():
        for index, w_count_class in enumerate(v):
            if w_count_class > 0:
                w_scores[k][index] = -log(w_count_class / c_scores[index])
            else:
                w_scores[k][index] = 0.0

    if verbose:
        for k, v in w_scores.iteritems():
            print k, v

    c_total = sum(c_scores)
    c_scores = [-log(c_score/ c_total) for c_score in c_scores]

    if verbose:
        print "Class scores after",  c_scores

    return w_scores, c_scores


####
# returns class and log probability
####
def naive_bayes_classifier(w_probs, c_probs, class_labels, x):
    global reverse_class_labels, unknown_label
    if not reverse_class_labels:
        reverse_class_labels = dict((index, class_label) for index, class_label in enumerate(class_labels))

    classification_prob = []
    for class_index, class_label in enumerate(class_labels):
        class_prob = c_probs[class_index]
        for word in word_tokenize(x):
            class_prob += w_probs[word][class_index] if word in w_probs else w_probs[unknown_label][class_index]
        classification_prob.append(class_prob)

    max_prob_index = int(argmax(classification_prob))

    return reverse_class_labels[max_prob_index], classification_prob[max_prob_index]
