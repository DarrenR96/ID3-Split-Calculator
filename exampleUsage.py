import ID3Split as ID3

dataSet = ID3.loadDataSet('data.csv')
print("numFeatures = " + str(len(dataSet[0][0: -1])))
entropy = ID3.calEntropy(dataSet)
maxvalue = ID3.computeInfoGains(dataSet)
input("Press any key to continue . . . \n")
quit()
