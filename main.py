import csv
import os


csv_file_name_relevant = os.path.join('example_data','Relevant.csv')
csv_file_name_not_relevant = os.path.join('example_data', 'Not_Relevant.csv')
folder_name = 'example_data'
with open(csv_file_name_relevant)  as csv_rel:
    csv_file_relevant = csv.reader(csv_rel)
    for row in csv_file_relevant:
        print(row)
with open(csv_file_name_not_relevant) as csv_notrel:
    csv_file_notrelevant = csv.reader(csv_notrel)
    for row in csv_file_notrelevant:
        print(row)


