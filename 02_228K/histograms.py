#!/usr/bin/python

import sys
import math
import numpy

#check command lines arguments
if len(sys.argv)!=8 :
    print("I need the name of the input file, X0, Y0,X1,Y1,NX,NY"); exit(1)

X0=float(sys.argv[2]); Y0=float(sys.argv[3])
X1=float(sys.argv[4]); Y1=float(sys.argv[5])
NX=float(sys.argv[6]); NY=float(sys.argv[7])

#open the file
try :
    input= open(sys.argv[1],'r')
except :
    print("Problems opening the input file"); exit(1)

#initialize variables
deltaX=(X1-X0)/NX; deltaY=(Y1-Y0)/NY
BinMatrix=numpy.zeros(int((NX)*(NY))).reshape(int(NX),int(NY))    
excluded=0
#start reading the input file:
#first column is the time
#second column is Rg
#third column is RMSD
numLines=0
accepted=0
while True:
    line=input.readline()
    if not line: break
    numLines +=1
    temp=line.split()
#coversion to float
    dataX=float(temp[0])
    dataY=float(temp[1])
#check whether the numbers are within range
#and update the matrix
    if (dataX < X1) & (dataX > X0): 
        if (dataY < Y1) & (dataY > Y0): 
            binX=int(math.floor((dataX-X0)/deltaX))       
            binY=int(math.floor((dataY-Y0)/deltaY))
            BinMatrix[binX,binY] += 1
            accepted +=1
        else: excluded +=1    
    else: excluded +=1            

input.close
#print histograms to file
output= open('FEL.dat','w')
i=0; j=0; sum=0
while i<NX:
    while j<NY:
#        if BinMatrix[i,j]==0:  #do not bother when no hit
#            j+=1
#            continue
        output.write('%s %s %s\n' % (X0+(i+0.5)*deltaX,Y0+(j+0.5)*deltaY,BinMatrix[i,j]))
        sum += BinMatrix[i,j]
        j+=1
    i +=1; j=0    
    output.write('\n')
output.close

#print normalized distribution to file
output= open('normFEL.dat','w')
i=0; j=0; norm=float(sum)
while i<NX:
    while j<NY:
#        if BinMatrix[i,j]==0:  #do not bother when no hit
#            j+=1
#            continue
        output.write('%s %s %s\n' % (X0+(i+0.5)*deltaX,Y0+(j+0.5)*deltaY,float(BinMatrix[i,j]/(norm*deltaX*deltaY))))
        j+=1
    i +=1; j=0    
    output.write('\n')
output.close

print("Lines read: ", numLines)
print("Points used: ",accepted)
print("Excluded Points: ", excluded)
print("Point inside matrix: ",sum)
