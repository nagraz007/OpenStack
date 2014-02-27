#Naga Raju Bhanoori

"""

"""

import sys
import os
import glob
import random
import subprocess

prevTag = "0"
prev2Tag = "0"
prevWord = "0"
prev2Word = "0"

def GetTag(word):
    # Uses MegaM
    wfile = open('megamClassify.tx', 'w')
    print word,
    wfile.write(word)
#     command = "./megam -nc -predict weights_pos multitron megamClassify.tx" 
#     os.system(command)
    args = ("./megam", "-nc", "-predict", "weights_pos", "multitron", "megamClassify.tx")
    #Or just:
    #args = "bin/bar -c somefile.xml -d text.txt -r aString -f anotherString".split()
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    print output

def ClassifySentence(line):
    global prevTag
    global prev2Tag
    outformat = ""
    line = line.split()
    for index in range(len(line)):
        print line[index]
        currentTag = GetTag(line[index] + " " + prevTag + " " + prev2Tag)
        outformat += line[index] + "/" + currentTag + " "
        prev2Tag = prevTag
        prevTag = currentTag
    print outformat.rstrip()

def main():
    for line in sys.stdin:
        try:
            ClassifySentence(line)
        except:
            break 

  # Get the name from the command line, using 'World' as a fallback.
  

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
