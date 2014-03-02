#Naga Raju Bhanoori

"""

"""

import sys
import os
import glob
import random
import subprocess
import percepclassify

prevTag = "0"
prev2Tag = "0"
prevWord = "0"
prev2Word = "0"
prevSuffix = "0"
prev2Suffix = "0"
nextWord = "0"
nextSuffix = "0"

classifiers = []
weightsList = []
sumList = []

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
    return classifiers[sumList.index(max(sumList))]

def FetchData(modelFile):
    rfile = open(modelFile, 'r')
    i = 0
    for line in rfile:
        i += 1
        line = line.rstrip()
        iline = line.split(' ')
        iclass = iline[0]
        classifiers.append(iclass)
        weightsList.append({})
        iline = iline[1:]
        iwindex = 0
        while (iwindex < len(iline)):
            weightsList[classifiers.index(iclass)][iline[iwindex]] = iline[iwindex+1]
            iwindex += 2
# def GetTag(word):
#     # Uses MegaM
#     wfile = open('megamClassify.tx', 'w')
#     print word,
#     wfile.write(word)
# #     command = "./megam -nc -predict weights_pos multitron megamClassify.tx" 
# #     os.system(command)
#     args = ("./megam", "-nc", "-predict", "weights_pos", "multitron", "megamClassify.tx")
#     #Or just:
#     #args = "bin/bar -c somefile.xml -d text.txt -r aString -f anotherString".split()
#     popen = subprocess.Popen(args, stdout=subprocess.PIPE)
#     popen.wait()
#     output = popen.stdout.read()
#     print output

def ClassifySentence(line):
    global prevTag
    global prev2Tag
    global prevWord
    global prev2Word
    global prevSuffix
    global prev2Suffix
    global nextSuffix
    global nextWord

    outformat = ""
    line = line.split()
    for index in range(len(line)):
        if index==0:
            prevTag = "0"
            prev2Tag = "0"
            prevWord = "0"
            prev2Word = "0"
            prev2Suffix = "0"
            prevSuffix = "0"
        if index +1 < len(line):
            nextWord = line[index+1]
            nextSuffix = line[index+1][-3:]
        else:
            nextWord = "0"
            nextSuffix = "0"
        feature = "w:"+ line[index] + " ws:"+ line[index][-3:] + " pw:" + prevWord + " pt:" + prevTag +" ps:" + prevSuffix + " p2w:" + prev2Word + " p2t:" + prev2Tag +" p2s:"+ prev2Suffix
        feature += " nw:" + nextWord + " ns:"+ nextSuffix
        currentTag = Predict(feature)
        outformat += line[index] + "/" + currentTag + " "
        prev2Tag = prevTag
        prevTag = currentTag
        prev2Word = prevWord
        prevWord = line[index]
        prev2Suffix = prevSuffix
        prevSuffix = line[index][-3:]
    print outformat.rstrip()

def main():
    if len(sys.argv) >= 1:
      modelFile = sys.argv[1]
    else:
        print 'Incorrect Usage!'
        sys.exit(1)
    FetchData(modelFile)
    for line in sys.stdin:
        ClassifySentence(line)
  # Get the name from the command line, using 'World' as a fallback.
  

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
