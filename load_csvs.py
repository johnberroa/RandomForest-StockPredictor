import os
import pandas
stocks_csv = list()
for dirname, dirnames, filenames in os.walk('./data/'):
    # print path to all filenames.
    for filename in filenames:
        stocks_csv.append(os.path.join(dirname, filename))
dfs = [pandas.read_csv(filename,sep=",",header=0,quotechar='"') for filename in stocks_csv]

print("csv_files loaded: ",len(dfs))