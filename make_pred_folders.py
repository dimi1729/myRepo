#!/usr/bin/python3.12

import os
import json
import pandas

prediction = 30
prev = prediction - 1
current_dir = "c:\\Users\\dtkal\\Downloads\\Lab Work\\make_pred_folders"

#remaining_file = current_dir + '\\pred_' + str(prev) + '\\yeast_pairs_minus_pred_' +str(prev) + '.json'
remaining_file = f"c:\\Users\\dtkal\\Downloads\\Lab_Work\\make_pred_folders\\pred_{prev}\\yeast_pairs_minus_pred_{prev}.json"
#print(remaining_file)
with open(remaining_file, 'r') as j:
    remaining_list = json.loads(j.read())

# uniprots_genename is dictionary in the form uniprot id : gene name
#df = pandas.read_csv(current_dir + '\\uniprot_genename.csv', usecols = ['Uniprot_id', 'Gene_name'])
df = pandas.read_csv("c:\\Users\\dtkal\\Downloads\\Lab_Work\\make_pred_folders\\uniprot_genename.csv", usecols = ['Uniprot_id', 'Gene_name'])
uniprots_genename = dict(df.values)

pred_list = []
non_pred_list = []

begs = ["E"]
stop = False

for pairs in remaining_list:
    pairs_list = pairs.split('_')
    if uniprots_genename[pairs_list[0]][0:1] in begs and stop==False:
        pred_list.append(pairs)
    elif uniprots_genename[pairs_list[1]][0:1] in begs and stop == False:
        pred_list.append(pairs)
    else:
        non_pred_list.append(pairs)



#json_file_name = current_dir +"\\pred_" + str(prediction) + "\\pred_" + str(prediction) + ".json"
#json_remaining_name = current_dir + "\\pred_" + str(prediction) + "\\yeast_pairs_minus_pred_" + str(prediction) + ".json"
json_file_name = f"c:\\Users\\dtkal\\Downloads\\Lab_Work\\make_pred_folders\\pred_{prediction}\\pred_{prediction}.json"
json_remaining_name = f"c:\\Users\\dtkal\\Downloads\\Lab_Work\\make_pred_folders\\pred_{prediction}\\yeast_pairs_minus_pred_{prediction}.json"

print(len(pred_list))
print(len(non_pred_list))
print(len(remaining_list))

with open(json_file_name, "w") as f:
    json.dump(pred_list, f)

with open(json_remaining_name, "w") as f:
    json.dump(non_pred_list, f)
