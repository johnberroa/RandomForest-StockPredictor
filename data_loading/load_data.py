# Credit to Justin Shenk for this code

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime


# Load S&P500 daily data
with open('symbols.txt', 'r') as file:
    symbols = file.read()
symbols = sorted([x.strip() for x in symbols.split('\n')])

stock_prices = []
data = pd.DataFrame()

<<<<<<< HEAD
# TODO: Add date checking to make sure values are aligned along same data range
=======
>>>>>>> parent of d499b79... Usage added and cleanup

for symbol in symbols:
    try:
        df = web.DataReader("{}".format(symbol), 'google')
        df['Symbol'] = symbol
        stock_prices.append(df)
        print("Loading", symbol)
    except Exception as e:
        print(e, "exception occured")
        pass
data = pd.concat(stock_prices)
data.to_csv('data.csv')