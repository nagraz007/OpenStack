#This script does the pre processing for pos data

import sys

infile = ""
outfile = ""
tagfile = ""

mode = sys.argv[1]
print "Mode : ",mode

if mode == "train":
    infile = open("train.pos","r")
    outfile = open("tf4prevpos_train.tx","w")
elif mode == "dev":
    infile = open("dev.pos","r")
    outfile = open("tf4prevpos_dev.tx","w")
    tagfile = open("tf4prevpos_devtags.tx","w")
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
                outfile.write(pairs[i][1]+" " +"w:"+pairs[i][0]+ " ws:"+pairs[i][0][-3:]+" wbs:"+pairs[i][0][-2:]+ " wp:"+pairs[i][0][:3]+" wbp:"+pairs[i][0][:2]+" ")
                #outfile.write(pairs[i][1]+" "+pairs[i][0]+"\n")
            else:
                outfile.write("w:"+pairs[i][0]+ " ws:"+pairs[i][0][-3:]+" wbs:"+pairs[i][0][-2:]+ " wp:"+pairs[i][0][:3]+" wbp:"+pairs[i][0][:2]+" ")
                tagfile.write(pairs[i][1]+"\n")
                #outfile.write("? "+pairs[i][0]+"\n")
                #outfile.write(pairs[i][1]+" "+pairs[i][0]+"\n")
                #tagfile.write(pairs[i][1]+"\n")
                
            if i==0:
                #outfile.write("pw:0 ps:0 p2w:0 ")
                outfile.write("pw:0 pt:0 pt2:0 ps:0 pbs:0 p2w:0 p2s:0 p2bs:0 pp:0 pbp:0 p2p:0 p2bp:0 ")
            elif i == 1:
                #outfile.write("pw:"+pairs[0][0]+" ps:"+pairs[0][0][-3:]+ " p2w:0" +" ")
                outfile.write("pw:"+pairs[0][0]+" pt:" + pairs[0][1]+ " pt2:0" + " ps:"+pairs[0][0][-3:]+ " pbs:"+pairs[0][0][-2:]+ " p2w:0 p2s:0 p2bs:0"+ " pp:"+pairs[0][0][:3]+ " pbp:"+pairs[0][0][:2]+ " p2p:0 p2bp:0" + " ")
            else:
                #outfile.write("pw:"+pairs[i-1][0]+ " ps:"+pairs[i-1][0][-3:]+ " p2w:"+pairs[i-2][0]+ " ")
                outfile.write("pw:"+pairs[i-1][0]+" pt:" + pairs[i-1][1] + " pt2:"+pairs[i-2][1]+ " ps:"+pairs[i-1][0][-3:]+ " pbs:"+pairs[i-1][0][-2:]+ " p2w:"+pairs[i-2][0]+ " p2s:"+pairs[i-2][0][-3:]+ " p2bs:"+pairs[i-2][0][-2:]+ " pp:"+pairs[i-1][0][:3]+ " pbp:"+pairs[i-1][0][:2]+" p2p:"+pairs[i-2][0][:3]+ " p2bp:"+pairs[i-2][0][:2]+ " ")
                #outfile.write(pairs[i-1][0] + " ")
             
            if i+2 < len(pairs):
                outfile.write("nw:"+pairs[i+1][0] + " ns:"+pairs[i+1][0][-3:]+ " nbs:"+pairs[i+1][0][-2:]+ " n2w:"+pairs[i+2][0] + " n2s:"+pairs[i+2][0][-3:]+ " n2bs:"+pairs[i+2][0][-2:] + " np:"+pairs[i+1][0][:3]+ " nbp:"+pairs[i+1][0][:2] + " n2p:"+pairs[i+2][0][:3]+ " n2bp:"+pairs[i+2][0][:2] +"\n")
            elif i+1 < len(pairs):
                outfile.write("nw:"+pairs[i+1][0] + " ns:"+pairs[i+1][0][-3:]+ " nbs:"+pairs[i+1][0][-2:]+ " n2w:0" + " n2s:0"+ " n2bs:0" + " np:"+pairs[i+1][0][:3]+ " nbp:"+pairs[i+1][0][:2] + " n2p:0"+ " n2bp:0" +"\n")
            else:
                outfile.write("nw:0 ns:0 nbs:0 n2w:0 n2s:0 n2bs:0 np:0 n2p:0 nbp:0 n2bp:0\n")
                #outfile.write(pairs[i][1]+" "+pairs[i][0]+"\n")
            
            
infile.close()            
outfile.close()
if mode == "dev" or mode == "test" :
    tagfile.close()
            
            
            
            
            
            
            
            
            
            
            
            
            
  
