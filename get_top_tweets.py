import re, sys, htmlentitydefs
import numpy,math
from decimal import *
from itertools import izip

emoticons_string = r"""
    (?:
      [<>]?
      [:;=8]                     # eyes
      [\-o\*\']?                 # optional nose
      [\)\]\(\[dDpP/\:\}\{@\|\\] # mouth      
      |
      [\)\]\(\[dDpP/\:\}\{@\|\\] # mouth
      [\-o\*\']?                 # optional nose
      [:;=8]                     # eyes
      [<>]?
    )"""#, re.VERBOSE | re.I | re.UNICODE)

html_tags_string = r"""<[^>]+>"""
html_entity_digit_re = re.compile(r"&#\d+;")
html_entity_alpha_re = re.compile(r"&\w+;")
amp = "&amp;"

emoticons_re = re.compile(emoticons_string, re.VERBOSE | re.I | re.UNICODE)
html_tags_re = re.compile(html_tags_string, re.VERBOSE | re.I | re.UNICODE)

def getStopWords(stopWordListFileName):
	stopWords = []
	fp = open(stopWordListFileName, 'r')
	for line in fp:
		line = line.strip()
		stopWords.append(line)
	fp.close()
	return stopWords


stopWords = getStopWords(sys.argv[2])

def html2unicode(self, s):
        """
        Internal metod that seeks to replace all the HTML entities in
        s with their corresponding unicode characters.
        """
        # First the digits:
	ents = set(html_entity_digit_re.findall(s))
        if len(ents) > 0:
            for ent in ents:
                entnum = ent[2:-1]
                try:
                    entnum = int(entnum)
                    s = s.replace(ent, unichr(entnum))	
                except:
                    pass
        # Now the alpha versions:
        ents = set(html_entity_alpha_re.findall(s))
        ents = filter((lambda x : x != amp), ents)
        for ent in ents:
            entname = ent[1:-1]
            try:            
                s = s.replace(ent, unichr(htmlentitydefs.name2codepoint[entname]))
            except:
                pass                    
            s = s.replace(amp, " and ")
        return s


#start process_tweet
def processTweet(tweet):

	#print(stopWords)
	temp = tweet.strip().split("\t")
	tweet = temp[0]
#Convert www.* or https?://* to URL
	tweet = re.sub('((www\.[\s]+)|(https?://[^\s]+))','URL',tweet)
#Convert @username to AT_USER
	tweet = re.sub('@[^\s]+','AT_USER',tweet)
#Remove additional white spaces
	tweet = re.sub('[\s]+', ' ', tweet)
#Replace #word with word
	tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
	
	
# do something with slangs and apostrophe words!!!
#handle not words
	line = ""
	for word in tweet.split(" "):
		if html_tags_re.search(word):
			continue
		if emoticons_re.search(word):  #check for emoticons
			line += word + " "
			continue
		word = word.strip('!;#$%&"\'()*+,-./:;<=>?@[]^_`{|}~').lower()
		if word in stopWords:
			continue
#elongated words
		word = re.sub(r'(.)\1{2,}',r'\1\1\1', word)
		line = line + word + " "
	return line.strip()

def dot_product(v1, v2):
    return sum(map(lambda x: x[0] * x[1], izip(v1, v2)))

def cosine_measure(v1, v2, len1, len2):
    prod = dot_product(v1, v2)
    #len1 = math.sqrt(dot_product(v1, v1))
    #len2 = math.sqrt(dot_product(v2, v2))
    return prod / (len1 * len2)

def compute_length(docs):
	length = []
	i =0
	for doc in docs:	
		length.append(math.sqrt(dot_product(docs[i], docs[i])))
		i +=1
	return length

def get_top_tweets(data):
	training = []
	tf = dict()
	idf = dict()
#file_reader = open(sys.argv[1],"r")
	count = 0
	for line in data:
		processed = processTweet(line)
		if processed == "":
			continue
		training.append(processed)
		#print(processed)
		tf[count] = dict()

		for word in processed.split(" "):
			if word in tf[count]:
				tf[count][word] +=1
			else:
				tf[count][word] =1
				if word in idf:
					idf[word] +=1
				else:
					idf[word] = 1
		count +=1
	#print(tf)
	#print(idf)
	#print(count)
	#file_reader.close()

	no_docs = count
	for doc in tf:
		for word in tf[doc]:
			tf[doc][word] *= math.log(Decimal(no_docs)/Decimal(idf[word]))

	i =0
	mat = []
	for doc in tf:
        	mat.append([])
        	for word in idf:
			if word in tf[doc]:
	                	mat[i].append(tf[doc][word])
			else:
				mat[i].append(0)
        	i +=1

	#print(mat)
	#print "Measure similarity!"

	length = compute_length(mat)

	sim_mat = []

#
	for i in range(0, no_docs):
		#print i
		sim_mat.append([])
		for j in range(0, i):
			sim = cosine_measure(mat[i], mat[j], length[i], length[j])
			sim_mat[i].append(sim)

#print(sim_mat)

#for i in range(0,no_docs):
#	most_similar_val = 0.0
#	most_similar_count = 0
#	for j in range(0,no_docs):
#		if sim_mat[i][j] > most_similar_val and i!=j:
#			most_similar_val =sim_mat[i][j]
#			most_similar_count = j
#	print str(most_similar_val) + "\t" + str(most_similar_count)

	sim_count = []
	most_similar_val = 0.5
	for i in range(0,no_docs):
		sim_count.append(0)
		for j in range(0,i):
			if sim_mat[i][j] > most_similar_val and i!=j:
				sim_count[i] +=1
		for j in range(i+1,no_docs):
			if sim_mat[j][i] > most_similar_val:
				sim_count[i] +=1
#		sim_count[i] +=1
		if sim_count[i] > 10:
			print str(sim_count[i]) +  " " + data[i].strip()
	

training = []
file_reader = open(sys.argv[1], "r")
for line in file_reader:	
	word = line.split(" ")
	if word[0] == "SEGMENT":
		get_top_tweets(training)
		print(line)
		training = []
	else:
		training.append(line)
	
