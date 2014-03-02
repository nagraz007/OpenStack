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

def ReadFiles(devfile, resultfile, actualfile, evalfile):
    r1 = open(resultfile, 'r')
    r2 = open(actualfile, 'r')
    r3 = open(devfile, 'r')
    w1 = open(evalfile, 'w')
    w = 0
    c = 0
    #w1 = open('finalsentiment.part2.out', 'w')
    for iline, jline, kline in zip(r1, r2, r3):
        
        iline = iline.replace('\t'," ")
        iline = iline.split(' ')
        iline = iline[0]
        #w1.write(iline + '\n')
        jline = jline.replace('\r', "")
        jline = jline.replace('\n', "")
        kline = kline.replace('\r', "")
        kline = kline.replace('\n', "")
        iline = iline.replace('\n', "")
        iline = iline.replace('\r', "")
        w1.write(kline + " " + jline + " " + iline + "\n")
def CalculateFScore():
    fscore = []
    for index in range(len(classifiers)):
        if classDict[index] != 0:
            precision = float(tclassDict[index])/classDict[index]
        else:
            precision = 1
        if aclassDict[index] != 0:
            recall = float(tclassDict[index])/ aclassDict[index]
        else:
            recall = 1
        if precision+recall != 0:
            fscore.append(float(2*precision*recall)/(precision + recall))
        else:
            fscore.append(0)
        print 'precision' + str(precision)
        print 'recall' + str(recall)
    print classifiers
    print fscore    
# Define a main() function that prints a little greeting.
def main():
  # Get the name from the command line, using 'World' as a fallback.
    if len(sys.argv) >= 5:
        devfile = sys.argv[1]
        resultfile = sys.argv[2]
        actualfile = sys.argv[3]
        evalfile = sys.argv[4]
#     if len(sys.argv) >= 1:
#         resultfile = '2'
#         #resultfile = 'out1.txt'
#         actualfile = '1'
    else:
        print 'Incorrect Usage!'
        sys.exit(1)
    ReadFiles(devfile, resultfile, actualfile, evalfile)
    print classifiers
    CalculateFScore()
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
