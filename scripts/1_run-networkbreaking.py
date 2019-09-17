#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 12:42:29 2017

@author: ChrisTokita

DESCRIPTION:
Script to run network-breaking cascade model on local machine
(single parameter combo, numerous replicates) 
"""
from model_networkbreaking import *

##########
# Set parameters
##########
n = 200 #number of individuals
k = 5 #mean degree on networks
gamma = -0.5 #correlation between two information sources
psi = 0.1 #proportion of samplers
p = 0.005 # probability selected individual forms new connection
timesteps = 10000 #number of rounds simulation will run
reps = 1 #number of replicate simulations

outpath = '../output/network_break/data/'


##########
# Run model
##########
for rep in np.arange(reps):
    sim_adjusting_network(replicate = rep, 
                          n = n, 
                          k = k, 
                          gamma = gamma, 
                          psi = psi, 
                          p = p, 
                          timesteps = timesteps,
                          outpath = outpath)
