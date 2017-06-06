import numpy as np
import pandas as pd

def RSI(dataframe, period):
    '''
    Computes the RSI of a given price series for a given period length
    :param dataframe:
    :param period:
    :return dataframe with rsi:
    '''

    # TODO:---
    # for symbol in dataframe:
    #     all_prices = dataframe[symbol].close
    # ---

    # dataframe["RSI"] = dataframe.apply(lambda row: RSI)
    rsi = []

    for stock in dataframe['Symbol'].unique():
        all_prices = dataframe[dataframe['Symbol'] == stock]['Close']
        diff = np.diff(all_prices) # length is 1 less than the all_prices
        rsi.append([None] * period) # because RSI can't be calculated until period prices have occured

        for i in range(len(diff) - period):
            avg_gain = diff[i:period + i]
            avg_loss = diff[i:period + i]
            avg_gain = abs(sum(avg_gain[avg_gain >= 0]) / period)
            avg_loss = abs(sum(avg_loss[avg_loss < 0]) / period)
            if avg_loss == 0:
                rsi.append(100)
            elif avg_gain == 0:
                rsi.append(0)
            else:
                rs = avg_gain / avg_loss
                rsi.append(100 - (100 / (1 + rs)))

    print("FIRST RSI THEN DATAFRAME LENGTH", len(rsi), len(dataframe))
    dataframe['RSI'] = rsi
    return dataframe
data = pd.read_csv('data.csv')
data = RSI(data, 14)
print(data.head())

def PROC(dataframe, period):
    '''
    Computes the PROC(price rate of change) of a given price series for a given period length
    :param dataframe:
    :param period:
    :return proc:
    '''

    # TODO:---
    # for symbol in dataframe:
    #     all_prices = dataframe[symbol].close
    # ---
    proc = [None] * period  # because PROC can't be calculated until period prices have occured
    for i in range(len(all_prices) - period):
        proc.append((all_prices[i + period] - all_prices[i]) / all_prices[i])

    return proc


def SO(dataframe):
    '''
    STOCHASTIC OSCIALLTOR
    Calculates fancy shit for late usage. Nice!

    EXAMPLE USAGE:
    data = pandas.read_csv("./data/ALL.csv", sep=",",header=0,quotechar='"')
    so = SO(data)
    print(so)

    '''
    so = []
    for i in range(len(dataframe)):
        C = dataframe.iloc[i]["<CLOSE>"]
        if(i > 13):
            h14 = dataframe.iloc[i-14:i]["<CLOSE>"].max()
            l14 = dataframe.iloc[i-14:i]["<CLOSE>"].min()
        else:
            h14 = dataframe.iloc[0:i]["<CLOSE>"].max()
            l14 = dataframe.iloc[0:i]["<CLOSE>"].min()
        so.append(100 * (C - l14) / (h14 - l14))

    return so

def Williams_R(dataframe):
    '''
    Williams %R
    Calculates fancy shit for late usage. Nice!

    EXAMPLE USAGE:
    data = pandas.read_csv("./data/ALL.csv", sep=",",header=0,quotechar='"')
    wr = Williams_R(data)
    print(wr)

    '''
    wr = []
    for i in range(len(dataframe)):
        C = dataframe.iloc[i]["<CLOSE>"]
        if(i > 13):
            h14 = dataframe.iloc[i-14:i]["<CLOSE>"].max()
            l14 = dataframe.iloc[i-14:i]["<CLOSE>"].min()
        else:
            h14 = dataframe.iloc[0:i]["<CLOSE>"].max()
            l14 = dataframe.iloc[0:i]["<CLOSE>"].min()
        wr.append((h14 - C) / (h14 - l14) * -100)

    return wr

def On_Balance_Volume(dataframe):
    '''
    Williams %R
    Calculates fancy shit for late usage. Nice!

    EXAMPLE USAGE:
    data = pandas.read_csv("./data/ALL.csv", sep=",",header=0,quotechar='"')
    wr = Williams_R(data)
    print(wr)

    '''
    obv = []
    obv.append(dataframe.iloc[0]["<VOL>"])
    for i in range(1,len(dataframe)):
        C_old = dataframe.iloc[i-1]["<CLOSE>"]
        C = dataframe.iloc[i]["<CLOSE>"]
        if(C > C_old):
            obv.append(obv[i-1]+dataframe.iloc[i]["<VOL>"])
        elif (C < C_old):
            obv.append(obv[i - 1] - dataframe.iloc[i]["<VOL>"])
        else:
            obv.append(obv[i-1])

    return obv

data = pd.read_csv("./data/ALL.csv", sep=",",header=0,quotechar='"')
print(data)
obv = On_Balance_Volume(data)
print(obv)
