##!/usr/bin/env python2
## -*- coding: utf-8 -*-
#"""
#Created on Tue Nov 27 18:06:28 2018
#
#@author: anamika
#"""
####FEATURE GENERATION:
##
####1. POS Tagging:
##import nltk
###nltk.download('averaged_perceptron_tagger')
##from nltk import word_tokenize
##t = word_tokenize("i love the fabric  will be great as a travel dress  pack easy   does not need to be iron really  substanti fabric   love it  i think it run larg sinc  i am rare a 2 at retailer  but i find that maev run all over the place   i am usual a 4 at retail and i got a 2 in this")
##
##tag = nltk.pos_tag(t)
###print tag
#
###CSV to JSON convert:
#import csv
#import json
#import io
#
#data = io.open('data/train.csv', 'r', encoding = 'utf-8-sig')
#
##csvFile = open('data/train.csv', 'r')
##data = csvFile.read().decode("utf-8-sig")
#jsonFile = open('final.json', 'w') 
#json_data = []
##Reader = csv.DictReader(csvFile)
#Reader = csv.DictReader(data)
#
#for row in Reader:
#    json1 = {}
#    json1['data'] = row['Review Text']
#    json1['label1'] = row['Sentiment']
#    json1['label2'] = []
#    json_data.append({
#            'Style': row['Style'],
#            'Fit': row['Fit'],
#            'Fabric' : row['Fabric'],
#            'Color' : row['Color'],
#            'Cost' : row['Cost']
#            })
#    json1['label2'] = json_data
#    json.dump(json1, jsonFile, indent = 2)
#    jsonFile.write('\n')
#    print (row)
#    break
#   
##for k, v in enumerate(Reader):
##    print k, v
#     
##DataFile = list(Reader)
##
##for row in DataFile:
##    json.dump(row, jsonFile, encoding = 'utf-8-sig')
##    jsonFile.write('\n')
#
##out = json.dumps( [ row for row in Data ] )
##jsonFile.write(out)
#
##for i in range (len(Data)):
##    jsonFile = json.dumps(Data)
#
#

##Plots for Baseline 3 versions:

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
x = ('Baseline' , 'Logreg' , 'SVM')
n = 6
x_pos = np.arange(3)
bar_width = 0.1
opacity = 0.7

f1_sentiment = [0.64, 0.69, 0.72, 0.8, 0.9, 0.96] 
f1_fit = 
f1_fabric =
f1_color = []
f1_style = 
f1_cost = []

plt.bar(x_pos, f1, bar_width, alpha = opacity, color = 'y', label = 'sentiment')
plt.bar(x_pos + bar_width, f1, bar_width, alpha = opacity, color = 'b', label = 'fit')
plt.bar(x_pos + bar_width, f1, bar_width, alpha = opacity, color = 'r', label = 'fabric')
plt.bar(x_pos + bar_width, f1, bar_width, alpha = opacity, color = 'g', label = 'color')
plt.bar(x_pos + bar_width, f1, bar_width,  alpha = opacity, color = 'c', label = 'style')
plt.bar(x_pos + bar_width, f1, bar_width,  alpha = opacity, color = 'm', label = 'cost')

plt.xticks(x_pos + bar_width, x)
plt.ylabel('F1 scores')
plt.title('Classifier comparison')
plt.legend()

plt.tight_layout() 
plt.show()







