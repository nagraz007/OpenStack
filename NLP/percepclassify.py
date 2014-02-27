#Naga Raju Bhanoori

"""

"""

import sys
import os
import glob
import random
import subprocess

classifiers = []
weightsList = []
sumList = []
its = 0

def Predict(line):
    features = line.split(' ')
    sumList = []
    for i in range(len(classifiers)):
        score = 0
        for feat in features:
            feat = feat.replace('\n', '')
            if not weightsList[i].has_key(feat):
                continue
            #print weightsList[i][feat]
            score += float(weightsList[i][feat])
        sumList.append(score)
    print classifiers[sumList.index(max(sumList))]

def FetchData(modelFile):
    rfile = open(modelFile, 'r')
    i = 0
    for line in rfile:
        i += 1
        line = line.rstrip()
        iline = line.split(' ')
#         if i == 1:
#             for iclass in iline:
#                 classifiers.append(iclass)
#                 weightsList.append({})
#         else:
        iclass = iline[0]
        classifiers.append(iclass)
        weightsList.append({})
        iline = iline[1:]
        iwindex = 0
        while (iwindex < len(iline)):
            #print iclass
            #print len(iline)
            if iwindex + 1 != len(iline):
                weightsList[classifiers.index(iclass)][iline[iwindex]] = iline[iwindex+1]
                #print iwindex
            if iwindex + 2 != len(iline):
                iwindex += 2
            else:
                #print iwindex
                iwindex += 1
                
def FetchDataFromModelFile(modelFile):
    rfile = open(modelFile, 'r')
    i = 0
    for line in rfile:
        i += 1
        line = line.rstrip()
        iline = line.split(' ')
        if i == 1:
            for iclass in iline:
                classifiers.append(iclass)
                weightsList.append({})
        else:
            feat = iline[0]
            iline = iline[1:]
            if len(iline) != len(classifiers):
                print 'Exception!!'
            for iwindex in range(len(iline)):
                weightsList[iwindex][feat] = iline[iwindex]
                

def main():
    
    if len(sys.argv) >= 1:
        modelFile = sys.argv[1]
    else:
        modelFile = "npercepmodel.ap"
    #print inMemSet[10]
    #FetchDataFromModelFile(modelFile)
    FetchData(modelFile)
    for line in sys.stdin:
        #try:
        #print line
        Predict(line)
        #except:
         #   break 

  # Get the name from the command line, using 'World' as a fallback.
  

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
