# Importing os and read csv file

# import different file directory
import os
# get information about current directory
print(os.getcwd())
# open different directory in which the data is stored
os.chdir(r'D:\Data Science\Corey Schafer')
# import the csv datasets
import csv
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # print out the data
    for names in csv_reader:
        print(names)
# open other directory
os.chdir(r'D:\Data Science')
# import the csv datasets
with open('new_names.csv', 'r') as csv_file2:
    csv_reader2 = csv.reader(csv_file2)
    # print out the data
    for line in csv_reader2:
        print(line)
