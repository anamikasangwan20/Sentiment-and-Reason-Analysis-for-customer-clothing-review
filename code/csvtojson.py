##CSV to JSON convert:
import csv
import json
import io

data = io.open('data/train.csv', 'r', encoding = 'utf-8-sig')

#csvFile = open('data/train.csv', 'r')
#data = csvFile.read().decode("utf-8-sig")
jsonFile = open('final.json', 'w') 
json_data = []
#Reader = csv.DictReader(csvFile)
Reader = csv.DictReader(data)

for row in Reader:
    json1 = {}
    json1['data'] = row['Review Text']
    json1['label1'] = row['Sentiment']
    json1['label2'] = []
    json_data.append({
            'Style': row['Style'],
            'Fit': row['Fit'],
            'Fabric' : row['Fabric'],
            'Color' : row['Color'],
            'Cost' : row['Cost']
            })
    json1['label2'] = json_data
    json.dump(json1, jsonFile, indent = 2)
    jsonFile.write('\n')
    print (row)
    break
