# Naga Raju Bhanoori
"""
Program to classify data from model file, Spits conditional probabilties
Doing Add one smoothing as dafault
"""

import sys
import math
import string
from symbol import except_clause

classifiers = []
classDict = {}
listDict = []
exceptions = set(string.punctuation)
defaultProbabilityList = [] # Will be the one calculated with smoothing

def removingPunctuations(word):
    if word in exceptions:
        return True
    return False

def getSumOfprobabilities(index, list):
    sum = 0
    if index == 2:
        return 0
    for ilist in list:
#         if not removingPunctuations(ilist):
#             ilist = ilist.strip(string.punctuation)
#             ilist = ilist.lower()
        if not listDict[index].has_key(ilist):
            listDict[index][ilist] = defaultProbabilityList[index]
        try:
            sum += float(listDict[index][ilist])
        except:
            #print listDict[index][ilist]
            sum += 0
    return sum

def Classifier(testFile):
    tfile = open(testFile, 'r')
    for line in tfile:
        iline = line.split(' ')
        probabilityList = []
        for index in range(len(classifiers)):
            sum = getSumOfprobabilities(index, iline)
            try:
                probabilityList.append(sum + math.log(float(classDict[classifiers[index]])))
            except:
                #print classDict[classifiers[index]]
                ij = 0
        print classifiers[probabilityList.index(max(probabilityList))]

def FetchDataFromModelFile(modelFile):
    global classDict
    global listDict
    rfile = open(modelFile, 'r')
    i = 0 # TODO: Add Valdations 
    for line in rfile:
        i += 1
        iline = line.split(' ')
        if i == 1:
            for iclass in iline:
                classifiers.append(iclass)
                listDict.append({})
        if i == 2:
            for index in range(len(iline)):
                classDict[classifiers[index]] = iline[index]
        if i == 3:
            for index in range(len(iline)):
                defaultProbabilityList.append(iline[index])
            break;
    for line in rfile:
        iline = line.split(' ')
        if len(iline) == 1 + len(classifiers):
            for index in range(len(iline)):
                if not index == 0:
                    listDict[index-1][iline[0]] = iline[index]
        else:
            print 'Bull Shit Value' + iline[0]
        
        
# Define a main() function that prints a little greeting.
def main():
  # Get the name from the command line, using 'World' as a fallback.
    if len(sys.argv) >= 3:
        modelFile = sys.argv[1]
        testFile = sys.argv[2]
#     if len(sys.argv) >= 1:
#         modelFile = 'sentiment.nb'
#         testFile = 'sentiment_testing.txt'
    else:
        print "Incorrect Usage!"
        sys.exit(1)
    FetchDataFromModelFile(modelFile)
    Classifier(testFile)
        



# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
