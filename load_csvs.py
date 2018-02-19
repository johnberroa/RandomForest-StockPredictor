import os
import pandas

# Loads the data and returns it as a pandas data frame
def generate_dataframe():
    stocks_csv = list()
    for dirname, dirnames, filenames in os.walk('./data/'):
        # print path to all filenames.
        for filename in filenames:
            stocks_csv.append(os.path.join(dirname, filename))
    dfs = [pandas.read_csv(filename,sep=",",header=0,quotechar='"') for filename in stocks_csv]
    return dfs
#print("csv_files loaded: ",len(dfs))
