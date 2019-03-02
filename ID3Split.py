# Libraries used
import csv
import math


# Returns dataSet within a list from csv file
def loadDataSet(file):
    dataSet = []
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for k in csv_reader:
            dataSet.append(tuple(k))
    return(dataSet)


# Returns information gain (entropy) of dataset
def calEntropy(dataSet):
    tuplesAmt = len(dataSet[1:])
    print("#Tuples = " + str(tuplesAmt))
    classes = []
    uniqueDictionary = {}
    for l in dataSet[1:]:
        classes.append(l[-1])
    uniqueClasses = classes
    uniqueClasses = list(set(uniqueClasses))
    for uc in uniqueClasses:
        uniqueDictionary[uc] = classes.count(uc)
    Info_D = 0
    print(uniqueDictionary)
    for ud in uniqueDictionary:
        Info_D += (uniqueDictionary[ud]/tuplesAmt) * \
            math.log(uniqueDictionary[ud]/tuplesAmt, 2)
        print("p"+str(uniqueClasses.index(ud)+1)+" = " +
              str(uniqueDictionary[ud])+"/"+str(tuplesAmt)+" = "
              + str(uniqueDictionary[ud]/tuplesAmt) +
              ", log2(p" + str(uniqueClasses.index(ud)+1)+") = "
              + str(math.log(uniqueDictionary[ud]/tuplesAmt, 2)
                    ) + ", p"+str(uniqueClasses.index(ud)+1)
              + " x log2(p" + str(uniqueClasses.index(ud)+1) + ") = "
              + str((uniqueDictionary[ud]/tuplesAmt) *
                    math.log(uniqueDictionary[ud]/tuplesAmt, 2)))
    Info_D = -Info_D
    print("Info(D) = " + str(Info_D)+"\n")
    return(Info_D)


# Returns selected data partition
def dataPartition(dataset, attIdx, v):
    dataSelTemp = []
    dataSel = []
    for ds in dataSet:
        dataSelTemp.append((ds[attIdx], ds[-1]))
    dataSel.append(dataSelTemp[0])
    for line in dataSelTemp:
        if (line[0] == v):
            dataSel.append(line)
    return(dataSel)


# Computes the information gains of selected data partitions
def computeInfoGains(dataset):
    totalTuple = len(dataset[1:])
    infoGainSet = []
    for col in range(0, (len(dataset[0])-1)):
        dCount = 0
        element = dataset[0][col]
        print("===== Splitting on "+str(element)+" =====")
        uniqueItems = []
        for l in dataset[1:]:
            uniqueItems.append(l[col])
        uniqueItems = set(uniqueItems)
        infoGain = 0
        for ui in uniqueItems:
            dCount = dCount + 1
            selDataSet = dataPartition(dataset, col, ui)
            propSelDataSet = (len(selDataSet)-1)/totalTuple
            print("|D"+str(dCount)+"| / |D| = "+str(len(selDataSet)-1) +
                  "/"+str(totalTuple) + " = "+str(propSelDataSet))
            selDataGain = calEntropy(selDataSet)
            infoGain += selDataGain*propSelDataSet
            print("Info["+str(dataset[0][col])+"] (D) = "+str(infoGain) + "\n")
        print("Gain("+str(dataset[0][col])+") = "+str(entropy) +
              " - "+str(infoGain) + " = "+str(entropy - infoGain))
        infoGainSet.append(entropy - infoGain)
    print("bestInfoGain = Gain(" +
          dataset[0][infoGainSet.index(max(infoGainSet))]+") = " + str(max(infoGainSet)))
    print("bestFeat index = "+str(infoGainSet.index(max(infoGainSet))))
    print("bestFeat name = "+dataset[0][infoGainSet.index(max(infoGainSet))])
    print("Attribute "+dataset[0][infoGainSet.index(max(infoGainSet))
                                  ]+" is selected as splitting attribute.")
    return(max(infoGainSet))


# Main Program
dataSet = loadDataSet('data.csv')
print("numFeatures = " + str(len(dataSet[0][0: -1])))
entropy = calEntropy(dataSet)
maxvalue = computeInfoGains(dataSet)
input("Press any key to continue . . . \n")
quit()
