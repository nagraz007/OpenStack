#This script does the pre processing for ner data

import sys

infile = ""
outfile = ""
tagfile = ""

mode = sys.argv[1]
print "Mode : ",mode

if mode == "train":
    infile = open("ner.esp.train","r")
    outfile = open("ner_train.txt","w")
elif mode == "dev":
    infile = open("ner.esp.dev","r")
    outfile = open("ner_dev.txt","w")
    tagfile = open("ner_devtags.txt","w")
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
            pairs[i] = pairs[i].split("/")
                       
        for i in range(0,len(pairs)):
        
            if mode =="train":
                outfile.write(pairs[i][2]+" "+"w:"+pairs[i][0]+" wt:"+pairs[i][1]+" ")
            else:
                outfile.write("w:"+pairs[i][0]+" wt:"+pairs[i][1]+" ")
                tagfile.write(pairs[i][2]+"\n")
                
            if i==0:
                outfile.write("pw:0 pt:0 pn:0 ")
            elif i == 1:
                outfile.write("pw:" + pairs[0][0]+ " pt:"+ pairs[0][1]+" pn:"+pairs[0][2]+" ")
            else:
                outfile.write("pw:" + pairs[i-1][0]+ " pt:"+ pairs[i-1][1]+" pn:"+pairs[i-1][2]+" ")
			
            if i+1 < len(pairs):
                outfile.write("nw:"+pairs[i+1][0] + " np:"+pairs[i+1][1]+"\n")
            else:
                outfile.write("nw:0 np:0\n")
infile.close()            
outfile.close()
if mode == "dev" or mode == "test" :
    tagfile.close()
            
            
            
            
            
            
            
            
            
            
            
            
            
  
