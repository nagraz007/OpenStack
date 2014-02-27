# Naga Raju Bhanoori
"""
Program to read directory and generating a txt file of classifier and features
Current Feature: Bag Of Words
"""

import sys
import os
import glob
import string

path = 'SPAM_test/'
#path = 'SPAM/'
#path = 'SENTIMENT_training/test/'
classifiers = ['SPAM', 'HAM']
#classifiers = ['POS', 'NEG']
exceptions = set(string.punctuation)

def removingPunctuations(word):
    if word in exceptions:
        return True
    return False

def preProcessor1():
	fclass = 'SPAM'
	#wfile = open('sentiment_test.txt', 'w')
	wfile = open('spam_test.txt', 'w')
	wfile1 = open('tmsactualResult.txt', 'w')
	count = 0
	lcount = 0
	files = glob.glob( os.path.join(path, '*.txt'))
	files.sort()

	for infile in files:
		#print "current file is: " + infile
		infile = os.path.basename(infile)
		count = count + 1
		for iclass in classifiers:
			if infile.find(iclass) >= 0:
				fclass = iclass
				lcount = lcount + 1
				break
		wfile1.write(fclass + '\n')
		#wfile.write('?' + ' ')		
		rfile = open(path + infile, 'r')
		for line in rfile:
			line = line.replace('<br />', '')
			line = line.replace('\r\n', '')
			line = line.replace('#', '')
			#line = line.replace('.', ' ')
			#line = line.replace('-', ' ')
			line = line.split(' ')
			for i in line:
 				if not removingPunctuations(i):
 					i = i.strip(string.punctuation)
 					i = i.lower()
				wfile.write(i + ' ')
		wfile.seek(-1,1)
		wfile.write('\n')
	print count
	print lcount

def preProcessor():
	#for infile in glob.glob( os.path.join(path, '*.*') ):
	#	print "current file is: " + infile
	fclass = 'SPAM'
	wfile = open('sentiment_finaltraining.txt', 'w')
	#wfile = open('10spam.txt', 'w')
	count = 0
	lcount = 0
	files = glob.glob( os.path.join(path, '*.txt'))
	files.sort()

	for infile in files:
		#print "current file is: " + infile
		infile = os.path.basename(infile)
		count = count + 1
		for iclass in classifiers:
			if infile.find(iclass) >= 0:
				fclass = iclass
				lcount = lcount + 1
				break
		wfile.write(fclass + ' ')		
		rfile = open(path + infile, 'r')
# 		for idata in read_data.split(' '):
# 			if idata.find('\r\n') < 0:			
# 				wfile.write(idata + ' ')	
# 		wfile.seek(-1,1)
# 		wfile.write('\n')
		for line in rfile:
			line = line.replace('<br />', '')
			line = line.replace('\r\n', '')
			line = line.replace('#', '')
			#line = line.replace('.', ' ')
			#line = line.replace('-', ' ')
			#line = line.replace('\n', '')
			#line = line.replace('\r', '')
			line = line.split(' ')
			for i in line:
 				if not removingPunctuations(i):
 					i = i.strip(string.punctuation)
 					i = i.lower()
				wfile.write(i + ' ')
		wfile.seek(-1,1)
		wfile.write('\n')
				
				
	print count
	print lcount
		
# Define a main() function that prints a little greeting.
def main():
  # Get the name from the command line, using 'World' as a fallback.
  preProcessor1()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
