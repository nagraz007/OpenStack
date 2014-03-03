#This script does the pre processing for ner data

import sys
import re

infile = ""
outfile = ""
tagfile = ""

mode = sys.argv[1]
print "Mode : ",mode

if mode == "train":
    infile = open("ner.esp.train","r")
    outfile = open("n3wner_train.tx","w")
elif mode == "dev":
    infile = open("ner.esp.dev","r")
    outfile = open("n3wner_dev.tx","w")
    tagfile = open("n3wner_devtags.tx","w")
    evalfile = open("n3wner_evalwords.tx","w")
elif mode == "test":
    print "Test Mode"

else:
    print "Invalid Mode Parameter"
    sys.exit()

data = infile.readlines()

    
if mode == "train"  or mode == "dev":
    for sent in data:
        #sent = sent.replace("#","")
        pairs =  sent.split()
        
        for i in range(0, len(pairs)):
            #pairs[i] = pairs[i].split()
            a = re.search("(.+)\/(.+)", pairs[i])
            b = re.search("(.+)\/(.+)", a.group(1))
            pairs[i] = [b.group(1), b.group(2),a.group(2)]
                       
        for i in range(0,len(pairs)):
            
            #print pairs[i]
            if pairs[i][0] != '' and pairs[i][0][0].isupper():
                isA='T'
            else:
                isA='F'
                
            if i-1 >= 0 and pairs[i-1][0] != '' and pairs[i-1][0][0].isupper():
                isB='T'
            else:
                isB='F'
            
            if i-2 >= 0 and pairs[i-2][0] != '' and pairs[i-2][0][0].isupper():
                isC='T'
            else:
                isC='F'

            allcap = '0'
            digit = '0'
            dash = '0'
            punc = '0'
            if re.match(r'^[A-Z]+$', pairs[i][0]):
                allcap = '1'
            else:
                allcap = '0'
            
            if re.match(r'.*[0-9].*', pairs[i][0]):
                digit = '1'
            
            if re.match(r'.*-.*', pairs[i][0]):
                dash = '1'

            if re.match(r'[.,;:?!-+\'"]', pairs[i][0]):
                punc = '1'
                
            if mode =="train":
                outfile.write(pairs[i][2]+" w:"+pairs[i][0]+ " wt:"+pairs[i][1]+" C:"+isA+" ws:"+pairs[i][0][-3:]+ " allcap:"+allcap + " digit:"+digit + " dash:"+dash+ " punc:"+punc+" ")

                #outfile.write(pairs[i][2]+" w:"+pairs[i][0]+ " wt:"+pairs[i][1]+" C:"+isA+" ws:"+pairs[i][0][-3:]+" ")
                #outfile.write(pairs[i][2]+" w:"+pairs[i][0]+ " wt:"+pairs[i][1]+"\n")
            else:
                outfile.write("w:"+pairs[i][0]+ " wt:"+pairs[i][1]+" C:"+isA+" ws:"+pairs[i][0][-3:]+ " allcap:"+allcap + " digit:"+digit + " dash:"+dash+ " punc:"+punc+" ")
                #outfile.write("w:"+pairs[i][0]+" wt:"+pairs[i][1]+" C:"+isA+" ws:"+pairs[i][0][-3:]+" ")
                evalfile.write(pairs[i][0] + "\n")
                #outfile.write("w:"+pairs[i][0]+" wt:"+pairs[i][1]+"\n")
                tagfile.write(pairs[i][2]+"\n")
                
            if i==0:
                outfile.write("pw2:0 pt2:0 pw:0 pt:0 pC:F p2C:F ps:0 ps2:0 pn:0 p2n:0 ")
            elif i == 1:
                #outfile.write("pw: "+pairs[0][0]+" pt:" +pairs[0][1]+" pn:"+pairs[0][2]+" ")
                outfile.write("pw2:0 "+ " pt2:0 "+ " pw:"+pairs[0][0]+" pt:" +pairs[0][1]+ " pC:"+isB+" p2C:"+isC+" ps:"+pairs[0][0][-3:]+ " ps2:0" + " pn:"+pairs[0][2] +" p2n:0"+" ")
            else:
                #outfile.write("pw: "+pairs[i-1][0]+" pt:" +pairs[i-1][1]+" pn:"+pairs[i-1][2]+" ")
                outfile.write("pw2:"+pairs[i-2][0]+" pt2:" +pairs[i-2][1]+ " pw:"+pairs[i-1][0]+" pt:" +pairs[i-1][1]+" pC:"+isB+" p2C:"+isC+" ps:"+pairs[i-1][0][-3:]+" ps2:"+pairs[i-2][0][-3:]+" pn:"+pairs[i-1][2]+" pn2:"+pairs[i-2][2]+" ")
             
            if i+2 < len(pairs):
                outfile.write("nw:"+pairs[i+1][0] + " nt:"+pairs[i+1][1]+" ns:"+pairs[i+1][0][-3:]+" n2w:"+pairs[i+2][0] + " n2t:"+pairs[i+2][1]+ "\n")
            elif i+1 < len(pairs):
                outfile.write("nw:"+pairs[i+1][0] + " nt:"+pairs[i+1][1]+" ns:"+pairs[i+1][0][-3:]+" n2w:0 n2t:0"+ "\n")
            else:
                outfile.write("nw:0 nt:0 ns:0 n2w:0 n2t:0\n")
            
            
infile.close()            
outfile.close()
if mode == "dev" or mode == "test" :
    tagfile.close()
            
            
            
            
            
            
            
            
            
            
            
            
            
  
