#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 15:50:31 2017

@author: yolandatiao


#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#
# Purpose: Find                                                               #
# Input: motif finding result mtf.csv                                         #
# Input dependent: Func_8_3_known_motif_to_csv                                #
# Last update: 7/17/17                                                        #
#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#

"""

#####------------------ Import START ------------------#####
import os # For changing directory
import subprocess # For calling bash 
import csv # For using csv writer
from astropy.io import ascii # For using ascii table to open csv
from astropy.table import Table, Column    # For using astropy table functions
import Tkinter,tkFileDialog
import glob
import seaborn as sns # For plotting
import matplotlib.pyplot as plt # For plotting
import pandas as pd # For using pandas in seaborn plot
import numpy as np # For using numpy matrix
#####------------------ Import END ------------------#####



#####------------------ Config START ------------------#####
codedir="/Volumes/Huitian/Exp174/codes"
wkdir="/Volumes/Huitian/Exp174/2_RNAseqMotifs"
#####------------------ Config END ------------------#####



#####------------------ Self Defined functions START ------------------#####
os.chdir(codedir)
import fc_basic_astropy_subprocess as fc

def tolower(listx):
    outlist=[]
    for i in listx:
        outlist.append(i.lower())
    return outlist

#####------------------ Self Defined functions END ------------------#####



#####------------------ Main function START ------------------#####
os.chdir(wkdir)
#----- Find gene names for transcription factor from RNAseq result
rnaseqfile="/Volumes/Huitian/Exp174/NormalizedGeneCounts.csv"
rtab=ascii.read(rnaseqfile)
rtab=fc.setcolnames(rtab)

famfile="/Volumes/Huitian/Exp174/2_RNAseqMotifs/Families.csv"
famtab=ascii.read(famfile)
famtab=fc.setcolnames(famtab)

rgnlist=list(rtab.columns[0]) # Genenamelist from RNAseq data
famtflist=list(famtab.columns[1])

rgnlistLOW=tolower(rgnlist)
famtflistLOW=tolower(famtflist)

rgnfind=[]
for i in famtflistLOW:
    i=i.split("[")[0]
    i=i.replace(")",",")
    i=i.replace("(",",")
    i=i.replace(" ","")
    i=i.replace("-","")
    i=i.replace("/","")
    ilist=i.split(",")
    ilist=filter(None, ilist)
    
    rgnx=None
    for n in ilist:   
        if n in rgnlistLOW:
            rgnx=n
    rgnfind.append(rgnx)

famtab["genename"]=rgnfind
ascii.write(famtab,"Families_genename.csv",format="csv", overwrite=True)

#####------------------ Main function END ------------------#####







































