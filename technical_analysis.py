import numpy as np

def RSI(dataframe, period):
    '''
    Computes the RSI of a given price series for a given period length
    :param dataframe:
    :param period:
    :return rsi:
    '''

    # TODO:---
    # for symbol in dataframe:
    #     all_prices = dataframe[symbol].close
    # ---

        diff = np.diff(all_prices) # length is 1 less than the all_prices
        rsi = [None] * period # because RSI can't be calculated until period prices have occured

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

        return rsi


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

# print(RSI([1,2,3,4,5,4,3,2,1], 2))
# print(RSI([1.00,2.00,3.00,4.00,5.00,4.00,3.00,2.00,1.00,1.00,2.00,3.00,
#      4.00,5.00,4.00,3.00,2.00,1.00,1.00,2.00,3.00,4.00,5.00,4.00,
#      3.00,2.00,1.00,2.00,3.00,4.00,5.00,4.00], 14))