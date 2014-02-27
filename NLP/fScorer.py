# Naga Raju Bhanoori

"""
Program takes 2 file inputs and return F-score
"""

import sys

classifiers = []
tclassDict = []
classDict = []
aclassDict = []
flist = []

def ReadFiles(resultfile, actualfile):
    r1 = open(resultfile, 'r')
    r2 = open(actualfile, 'r')
    w = 0
    c = 0
    #w1 = open('finalsentiment.part2.out', 'w')
    for iline, jline in zip(r1, r2):
        
        #iline = iline.replace('\t'," ")
        #iline = iline.split(' ')
        #iline = iline[0]
        #w1.write(iline + '\n')
        jline = jline.replace('\r', "")
        jline = jline.replace('\n', "")
        iline = iline.replace('\n', "")
        iline = iline.replace('\r', "")
        if not iline in classifiers:
            classifiers.append(iline)
        if not jline in classifiers:
            classifiers.append(jline)
        iindex = classifiers.index(iline)
        jindex = classifiers.index(jline)
        while len(tclassDict) < len(classifiers):
            tclassDict.append(0)
        while len(classDict) < len(classifiers):
            classDict.append(0)
        while len(aclassDict) < len(classifiers):
            aclassDict.append(0)

        if iindex == jindex:
            tclassDict[iindex] += 1 
            c += 1
        w += 1
        classDict[iindex] += 1
        aclassDict[jindex] += 1
    print str(c) + " " + str(w)
def CalculateFScore():
    fscore = []
    for index in range(len(classifiers)):
        precision = float(tclassDict[index])/classDict[index]
        recall = float(tclassDict[index])/ aclassDict[index]
        fscore.append(float(2*precision*recall)/(precision + recall))
        print 'precision' + str(precision)
        print 'recall' + str(recall)
    print classifiers
    print fscore    
# Define a main() function that prints a little greeting.
def main():
  # Get the name from the command line, using 'World' as a fallback.
    if len(sys.argv) >= 3:
      resultfile = sys.argv[1]
      actualfile = sys.argv[2]
#     if len(sys.argv) >= 1:
#         resultfile = '2'
#         #resultfile = 'out1.txt'
#         actualfile = '1'
    else:
        print 'Incorrect Usage!'
        sys.exit(1)
    ReadFiles(resultfile, actualfile)
    print len(classifiers)
    #CalculateFScore()
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
