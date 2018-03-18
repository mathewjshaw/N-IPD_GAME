# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 10:09:06 2016

@author: Matt , Dongping
"""
from random import shuffle
from random import randint
from random import uniform 
import matplotlib.pyplot as plt
import numpy as np

def G(n,k):  
    stubs = list(range(n))
    stubs = stubs * k
    
    
    shuffle(stubs)
    net = {i:[0,[],[randint(0,1)],-1] for i in range(n)}
    
    m=0
    while(m<len(stubs)-1):
        j = stubs[m+1]
        i = stubs[m]
        net[i][1].append(j)
        net[j][1].append(i)
        net[i][0] = net[i][0] + 1
        net[j][0] = net[j][0] + 1
        m += 2
    return net


game = G(1000,4)
R = .9


for i in range(1000):
    ourChoice = game[i][2][0]
    tempList = game[i][1]
    j = 0
    # C = 1 and D = 0
    totalPayoff = 0
    for neighbor in (tempList):
        neighborChoice = game[neighbor][2][0]
        if (neighborChoice == 0 and ourChoice == 0):
            totalPayoff += 0
            
        if (neighborChoice == 0 and ourChoice == 1):
            totalPayoff += 0
            
        if (neighborChoice == 1 and ourChoice == 0):
            totalPayoff += 1+R            
            
        if (neighborChoice == 1 and ourChoice == 1):
            totalPayoff += 1
            
    game[i][3] = totalPayoff

def roundX(x):
    current = 0
    while(current < x):
        for i in range(1000):
            neighbors = game[i][1]
            j = 0
            randNeighbor = neighbors[randint(0,3)]
            neighborPayoff = game[randNeighbor][3]
            ourPayoff = game[i][3]
            ourChoice = game[i][2][current]
            # C = 1 and D = 0
                
            
            
            
            if(neighborPayoff > ourPayoff):
                probSwap = (neighborPayoff-ourPayoff)/((R+1)*4)
                choice = uniform(0,1)
                
                if(choice <= probSwap):
                    ourChoice = game[randNeighbor][2][current]
            
            game[i][2].append(ourChoice)
        current = current + 1
             
             
             
        for i in range(1000): 
            newPayoff = 0
            neighbors = game[i][1]
            ourChoice = game[i][2][-1]
            for neighbor in (neighbors):
                neighborChoice = game[neighbor][2][-1]
                if (neighborChoice == 0 and ourChoice == 0):
                    newPayoff += 0
                    
                elif (neighborChoice == 0 and ourChoice == 1):
                    newPayoff += 0
                        
                elif (neighborChoice == 1 and ourChoice == 0):
                    newPayoff += (1+R)
                            
                elif (neighborChoice == 1 and ourChoice == 1):
                    newPayoff += 1
                
            game[i][3] = newPayoff
    return game

roundX(999)

##RESULTS!
totalCoop = 0
for i in range(1000):
    totalCoop += game[i][2][999]
    percentCoop = totalCoop/1000
    


    
    