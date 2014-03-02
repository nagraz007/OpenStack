#Naga Raju Bhanoori

"""

"""

import sys
import os
import glob
import random
import subprocess

inMemSet = []
classifiers = []
weightsList = []
snapList = []
sumList = []
featureList = {}
its = 0
asumList = []

def AccumulateSum():
    for i in range(0, len(classifiers)):
        for key in weightsList[i]:
            if key in asumList[i]:
                asumList[i][key] += weightsList[i][key]
            else:
                asumList[i][key] = weightsList[i][key]
        
# 
# def GenerateModel(modelFile, iterations):
#     wfile = open(modelFile, 'w')
# #     for iclass in classifiers:
# #         wfile.write(iclass + " ")
#     #wfile.write('\n')
#     for i in range(0, len(classifiers)):
#         wfile.write(classifiers[i] + ' ')
#         for feat in featureList:
#             wfile.write(feat + ' ')
#             sum = 0
#             for iweightsList in snapList:
#                 if iweightsList[i].has_key(feat):
#                     sum += iweightsList[i][feat]
#             if iterations != len(snapList):
#                 print "Exception!"
#                 sys.exit(1)
#             wfile.write(str(float(sum)/iterations) + ' ')
#             #wfile.write(str(snapList[-1][i][feat]) + ' ')
#         wfile.write('\n')
        
    

def CalculateAverageAndGenerateModel(iterations):
    wfile = open('naga.ap', 'w')
    for iclass in classifiers:
        wfile.write(iclass + " ")
    wfile.write('\n')
    for feat in featureList:
        wfile.write(feat + ' ')
        for i in range(len(classifiers)):
            sum = 0
            for iweightsList in snapList:
                if iweightsList[i].has_key(feat):
                    sum += iweightsList[i][feat]
            wfile.write(str(float(sum)/iterations) + ' ')
            #wfile.write(str(snapList[-1][i][feat]) + ' ')
        wfile.write('\n')
    
def CalculateAverageAndGenerateModel1(modelFile, iterations):
    wfile = open(modelFile, 'w')
    for i in range(0, len(classifiers)):
        wfile.write(classifiers[i] + ' ')
        for key in asumList[i]:
            wfile.write(key + ' ')
            sum = asumList[i][key]
            wfile.write(str(float(sum)/iterations) + ' ')
        wfile.write('\n')

def updateFeatures(features, predictedClass, actualClass):
    pIndex = getIndexOfClassifier(predictedClass)
    aIndex = getIndexOfClassifier(actualClass)
    for feat in features:
        feat = feat.replace('\n', '')
        if feat in weightsList[pIndex]:
            weightsList[pIndex][feat] = 0
        if feat in weightsList[aIndex]:
            weightsList[aIndex][feat] = 0
        weightsList[pIndex][feat] -= 1
        weightsList[aIndex][feat] += 1

def Predict(features):
    sumList = []
    for i in range(0, len(classifiers)):
        score = 0
        for feat in features:
            feat = feat.replace('\n', '')
            if feat in weightsList[i]:
                score += weightsList[i][feat]
            else:
                weightsList[i][feat] = 0
        sumList.append(score)
    return classifiers[sumList.index(max(sumList))]
    

def getIndexOfClassifier(className):
    if className in classifiers:
        return classifiers.index(className)
    else:
        print "Exception!"

def RunIterations(iterations):
    global its
    print iterations
    for i in range(iterations):
        updates = 0
        its += 1
        print its
        #random.shuffle(inMemSet)
        print its
        for data in inMemSet:
            # this is actual list of features
            if data[0] not in classifiers:
                classifiers.append(data[0])
                weightsList.append({})
                asumList.append({})
            actualClass = data[0]
            features = data[1:]
            predictedClass = Predict(features)
            if predictedClass != actualClass:
                updateFeatures(features, predictedClass, actualClass)
                updates += 1
        print "Error: " + str(float(updates)/len(inMemSet)) +" " +str(updates)
        print classifiers
        #snapList.append(weightsList)
        AccumulateSum()
        if updates == 0:
            break
        random.shuffle(inMemSet)

def ReadInput():
    line = line.split(" ")
    print line[0]
    if line[0] not in classifiers:
        classifiers.append(line[0])
        weightsDict.append({})

def main():
    for line in sys.stdin:
        line = line.rstrip()
        line = line.split(" ")
        inMemSet.append(line)
    if len(sys.argv) == 3:
        iterations = sys.argv[1]
        modelFile = sys.argv[2]
    else:
        iterations = 20
        modelFile = 'npercepmodel.ap'
    #print inMemSet[10]
    RunIterations(int(iterations))
    #print classifiers
    #GenerateModel(modelFile, its)
    CalculateAverageAndGenerateModel1(modelFile, its)
    print its

  # Get the name from the command line, using 'World' as a fallback.
  

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
