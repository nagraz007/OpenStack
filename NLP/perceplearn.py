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
    for feat in featureList:
        for i in range(len(classifiers)):
            if not weightsList[i].has_key(feat):
                weightsList[i][feat] = 0
            if not asumList[i].has_key(feat):
                asumList[i][feat] = 0
            asumList[i][feat] += weightsList[i][feat]

def GenerateModel(modelFile, iterations):
    wfile = open(modelFile, 'w')
#     for iclass in classifiers:
#         wfile.write(iclass + " ")
    #wfile.write('\n')
    for i in range(len(classifiers)):
        wfile.write(classifiers[i] + ' ')
        for feat in featureList:
            wfile.write(feat + ' ')
            sum = 0
            for iweightsList in snapList:
                if iweightsList[i].has_key(feat):
                    sum += iweightsList[i][feat]
            wfile.write(str(float(sum)/iterations) + ' ')
            #wfile.write(str(snapList[-1][i][feat]) + ' ')
        wfile.write('\n')
        
    

def CalculateAverageAndGenerateModel(iterations):
    wfile = open('percepmodel_tf_test1.ap', 'w')
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
    
def CalculateAverageAndGenerateModel1(iterations):
    wfile = open('percepmodel_tf_v4.0.ap', 'w')
    for iclass in classifiers:
        wfile.write(iclass + " ")
    wfile.write('\n')
    for feat in featureList:
        wfile.write(feat + ' ')
        for i in range(len(classifiers)):
            sum = 0
            if asumList[i].has_key(feat):
                sum = asumList[i][feat]
            wfile.write(str(float(sum)/iterations) + ' ')
            #wfile.write(str(snapList[-1][i][feat]) + ' ')
        wfile.write('\n')

def updateFeatures(features, predictedClass, actualClass):
    pIndex = getIndexOfClassifier(predictedClass)
    aIndex = getIndexOfClassifier(actualClass)
    for feat in features:
        feat = feat.replace('\n', '')
        if not weightsList[pIndex].has_key(feat):
            weightsList[pIndex][feat] = 0
        if not weightsList[aIndex].has_key(feat):
            weightsList[aIndex][feat] = 0
        weightsList[pIndex][feat] -= 1
        weightsList[aIndex][feat] += 1

def Predict(features):
    sumList = []
    for i in range(len(classifiers)):
        score = 0
        for feat in features:
            feat = feat.replace('\n', '')
            if not featureList.has_key(feat):
                featureList[feat] = feat
            if weightsList[i].has_key(feat):
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
        random.shuffle(inMemSet)
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
        print "err" + str((float(updates)/len(inMemSet)))
        snapList.append(weightsList)
        #AccumulateSum()
        if updates == 0:
            break

def ReadInput():
    line = line.split(" ")
    print line[0]
    if line[0] not in classifiers:
        classifiers.append(line[0])
        weightsDict.append({})

def main():
    for line in sys.stdin:
        try:
            line = line.rstrip()
            line = line.split(" ")
            inMemSet.append(line)
            
        except:
            break 
    if len(sys.argv) == 3:
        iterations = sys.argv[1]
        modelFile = sys.argv[2]
    else:
        iterations = 20
        modelFile = 'npercepmodel.ap'
    #print inMemSet[10]
    RunIterations(int(iterations))
    GenerateModel(modelFile, its)
    #CalculateAverageAndGenerateModel(its)
    print its

  # Get the name from the command line, using 'World' as a fallback.
  

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
