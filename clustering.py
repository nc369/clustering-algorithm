#!/usr/bin/env python
# coding: utf-8

# In[71]:


import numpy as np
import random as rd
import matplotlib.pyplot as plt 


# In[72]:


def distance(a, b):
    return np.sqrt(np.sum(np.square([a_i - b_i for a_i, b_i in zip(a, b)])))


# In[73]:


def cluster(data,k=10,iterations=100,epsilon=1):
    
    data_pts = data.shape[0]
    centroids = data[rd.sample(range(data_pts),k),:]
    id_ = [0]*data_pts
    
    for i in range(iterations):
        clas = [[] for i in range(k)]
        for pt in range(data_pts):
            dist = list(map(lambda x: distance(x,data[pt]),centroids))
            ind = dist.index(min(dist))
            clas[ind].append(data[pt])
            id_[pt] = ind
            
        temp_centroids = list( map(lambda x: np.mean(x,axis=0),clas ) )
        check = [distance(a_i,b_i) for a_i,b_i in zip(centroids , temp_centroids)] 
        
        
        centroids = temp_centroids
        if np.sum(check)<epsilon:
            break
    
    return np.array(centroids),id_






