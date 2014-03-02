#This is the python code for the learning phase of the perceptron
import sys
import copy
import random


def main():
    trainfile = open(sys.argv[1],"r")
    outfile = open(sys.argv[2],"w")
    
    tdata,labelset = getTrainingData(trainfile)
    trainfile.close()
    w = getInitialWeights(labelset)
    
    labelset.sort()
    '''
    print labelset    
    print len(labelset)
    '''
    w = learn(20,tdata,w)
        
    createModelFile(outfile,w)
    outfile.close()
    
def learn(n,tdata,w):
    wavg = copy.deepcopy(w)
    wprev = copy.deepcopy(w)
   
    for i in range(n):
        print "Iteration ", i+1
        falsenum = 0
        for data in tdata:
            y = data["Label"]
            x = data["Features"]
            
            z = predict(w,x)
            if z != y:
                falsenum += 1
                for feat in x:
                    if feat in w[z]:
                        w[z][feat] = w[z][feat] - 1 
                    else :
                        w[z][feat] = -1
                        
                    if feat in w[y]:
                        w[y][feat] = w[y][feat] + 1 
                    else :
                        w[y][feat] = 1  
        error = falsenum/float(len(tdata))       
        print "Error : ",falsenum,"/",len(tdata)," = ",error
        flag = checkConvergence(w,wprev)
        
        if flag == True:
            print "Weight Vectors Converged"
            break
        else:
            wavg = updateW(w,wavg)    
            copy.deepcopy(w)
        random.shuffle(tdata)
    if flag == True:
        num = i
    else:
        num = n
               
    for label in wavg:
        for feat in wavg[label]:
            wavg[label][feat] = wavg[label][feat]/float(num)    
                        
    return wavg

def predict(w,features):
    maxval = ["?",-1]
    for label in w:
        temp = 0
        wi = w[label]
        for feat in features:
            if feat in wi:
                temp += wi[feat]
        if temp > maxval[1]:
            maxval = [label,temp]
    return maxval[0]    
    
def checkConvergence(w,wprev):
    converged = True
    for label in w:    
        if label not in wprev:
            converged = False
        elif w[label] != wprev[label]:
            converged = False
    return converged     
         
def updateW(w,wavg):
        
    for label in w:    
                    
        for feat in w[label]:
            if feat in wavg[label]:
                wavg[label][feat] += w[label][feat]
            else:
                wavg[label][feat] = w[label][feat]

    return wavg
    
    
def getTrainingData(trainfile):
    tdata = []
    labelset = []
    line = trainfile.readline()
    while len(line) > 0:
    
        tempD = {}
        line = line.split()
        tempD["Label"] = line[0]
                
        if line[0] not in labelset:
            labelset.append(line[0])
            
        line = line[1:]
        tempD["Features"] = line
        
        tdata.append(tempD)

        line = trainfile.readline()
    return tdata,labelset        

def getInitialWeights(labelset):
    w = {}
    for label in labelset:
        w[label] = {}
    return w

def createModelFile(outfile,w):
    print "Creating Model File"
    for label in w:
        outfile.write(label+" ")
        for feat in w[label]:
            outfile.write(str(feat)+"/"+str(w[label][feat])+" ")
        outfile.write("\n")
    print "Model File Created"




main()
