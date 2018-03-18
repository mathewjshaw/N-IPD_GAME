# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:23:07 2016

@author: Matt
"""
from random import shuffle
from random import randint
from random import uniform 
import matplotlib.pyplot as plt
import numpy as np 
def G(n,p):
    net = {i:[0,[],[randint(0,1)],-1] for i in range(n)}
    for i in net:
        for j in range(i+1,n):
            x=np.random.random()
            if(x<=p):
                net[i][1].append(j)
                net[j][1].append(i)
                net[i][0]=net[i][0]+1
                net[j][0]=net[j][0]+1
    return net
            
    
game = G(1000,.1)

R = 0.5




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
            if(len(neighbors)==0):
                continue
                
            j = 0
            randNeighbor = neighbors[randint(0,len(neighbors)-1)]
            neighborPayoff = game[randNeighbor][3]
            ourPayoff = game[i][3]
            ourChoice = game[i][2][current]
            # C = 1 and D = 0
                
            if(game[randNeighbor][0] >= game[i][0]):
                kMax = game[randNeighbor][0]
            elif(game[randNeighbor][0] < game[i][0]):
                kMax = game[i][0]
                

            if(neighborPayoff > ourPayoff):
                probSwap = (neighborPayoff-ourPayoff)/((R+1)*kMax)
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


totalCoop = 0
totalPlayers = 1000
for i in range(1000):
    if(len(game[i][2]) == 1):
        totalPlayers = totalPlayers - 1
        continue
        
    totalCoop += game[i][2][999]
    percentCoop = totalCoop/totalPlayers
    

