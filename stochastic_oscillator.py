import pandas


#input: best would be 14 rows of data. Less ok, more unnecessary
def stochastic_oscillator(trData):
    #cut pandas frame after 14 rows
    C = trData[0]["CLOSING"]
    h14 = trData.closing.max()
    l14 = trData.closing.min()

    #Implement real places of the values
    return 100 * (C - l14)/(h14-l14)

T =stochastic_oscillator(data)
print(T)