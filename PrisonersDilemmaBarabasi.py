# -*- coding: utf-8 -*-
"""
Created on Tue May  3 10:20:41 2016

@author: Matt
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 14:36:01 2016

@author: mcliston
"""

import numpy as np
import networkx as nx
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import collections
import copy
from random import shuffle

from random import randint
from random import uniform 
import matplotlib.pyplot as plt

R = 0



C=nx.barabasi_albert_graph(1000,3)
l=list()
l.extend(C.degree().values())

stubs = list()

i=0

while(i<1000):
    j=0
    while(j<l[i]):
        stubs.append(i) 
        j+=1
    i+=1
        


stubs_1 = copy.copy(stubs)
shuffle(stubs)

def G(n,k):
    
    net = {i:[0,[],[randint(0,1)],-1] for i in range(n)}
    
    m=0
    while(m<len(stubs)-1):
        j = stubs[m+1]
        i = stubs[m]
        net[i][1].append(j)
        net[j][1].append(i)
        net[i][0] = net[i][0] +1
        net[j][0] = net[j][0] +1
        m += 2
        
    return(net)
    
    
    
game = G(1000,4)


i=0
netDegrees=list()
while(i<len(game)):
    netDegrees.append(game[i][0])
    i+=1

degree_sequence=sorted(netDegrees)
degreeCount=collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.90, color='g')

plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d+0.4 for d in deg])
ax.set_xticklabels(deg)







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
    
