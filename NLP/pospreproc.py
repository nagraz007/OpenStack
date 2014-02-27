#This script does the pre processing for pos data

import sys

infile = ""
outfile = ""
tagfile = ""

mode = sys.argv[1]
print "Mode : ",mode

if mode == "train":
    infile = open("train.pos","r")
    outfile = open("tf1prevpos_train.tx","w")
elif mode == "dev":
    infile = open("dev.pos","r")
    outfile = open("tf1prevpos_dev.tx","w")
    tagfile = open("tf1prevpos_devtags.tx","w")
elif mode == "test":
    print "Test Mode"

else:
    print "Invalid Mode Parameter"
    sys.exit()

data = infile.readlines()

    
if mode == "train"  or mode == "dev":
    for sent in data:
        
        pairs =  sent.split()
        
        for i in range(0, len(pairs)):
            pairs[i] = pairs[i].split("/")
                       
        for i in range(0,len(pairs)):
            
#             pairs[i][0] = pairs[i][0].replace('#', '0')
#             pairs[i][1] = pairs[i][1].replace('#', '0')
#             
#             if i+1 < len(pairs):
#                 pairs[i+1][0] = pairs[i+1][0].replace('#', '0')
#                 pairs[i+1][1] = pairs[i+1][1].replace('#', '0')
            
            if mode =="train":
                outfile.write(pairs[i][1]+" " +"w:"+pairs[i][0]+ " ws:"+pairs[i][0][-3:]+" ")
                #outfile.write(pairs[i][1]+" "+pairs[i][0]+"\n")
            else:
                outfile.write("w:"+pairs[i][0]+ " ws:"+pairs[i][0][-3:]+" ")
                tagfile.write(pairs[i][1]+"\n")
                #outfile.write("? "+pairs[i][0]+"\n")
                #outfile.write(pairs[i][1]+" "+pairs[i][0]+"\n")
                #tagfile.write(pairs[i][1]+"\n")
                
            if i==0:
                outfile.write("pw:0 pt:0 pt2:0 ")
            elif i == 1:
                outfile.write("pw:"+pairs[0][0]+" pt:" + pairs[0][1]+ " pt2:0 ")
            else:
                outfile.write("pw:"+pairs[i-1][0]+" pt:" + pairs[i-1][1] +" "+ "pt2:"+pairs[i-2][1]+ " ")
                #outfile.write(pairs[i-1][0] + " ")
             
            if mode =="train":
                if i+1 < len(pairs):
                    outfile.write("nw:"+pairs[i+1][0] + " ns:"+pairs[i+1][0][-3:]+"\n")
                else:
                    outfile.write("\n")
                #outfile.write(pairs[i][1]+" "+pairs[i][0]+"\n")
            else:
                if i+1 < len(pairs):
                    outfile.write("nw:"+pairs[i+1][0]+ " ns:"+pairs[i+1][0][-3:]+ "\n")
                else:
                    outfile.write("\n")
            
infile.close()            
outfile.close()
if mode == "dev" or mode == "test" :
    tagfile.close()
            
            
            
            
            
            
            
            
            
            
            
            
            
  
