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

#####------------------ Self Defined functions END ------------------#####



#####------------------ Main function START ------------------#####
os.chdir(wkdir)
#----- Make annotated family table
infile="HomerMotifs.csv"
outfile="HomerMotif_anno.csv"
with open(infile, "r") as fin:
    rfin=csv.reader(fin)
    next(rfin)
    with open (outfile, "w") as fout:
        wfout=csv.writer(fout, delimiter=",")
        wfout.writerow(["Motif","GeneName","GeneFamily"])
        for row in rfin:
            rowstr=row[0]
            rowname=rowstr.split("/")[0]
            if "(" in rowname:
                rowGname=rowname.split("(")[0]
                rowFname=rowname.split("(")[1].replace(")","")
            else:
                rowGname=rowname
                rowFname="NaN"
            rowGname=rowGname.replace(":",",")
            rowFname=rowFname.replace(":",",")
            rowGname=rowGname.replace("|","")
            rowFname=rowFname.replace("|","")
            rowGnamelist=rowGname.split(",")
            rowFnamelist=rowFname.split(",")
            rowGnamelist=filter(None, rowGnamelist)
            rowFnamelist=filter(None, rowFnamelist)
            #print rowGnamelist
            #print rowFnamelist
            if len(rowGnamelist) > 1 and len(rowFnamelist) >1:
                for x in xrange(0,len(rowGnamelist)):
                    wfout.writerow([rowstr, rowGnamelist[x],rowFnamelist[x]])
            else:
                wfout.writerow([rowstr, rowGname,rowFname])

#----- Annotate if gene is in RNAseq result
infile="/Volumes/Huitian/Exp174/2_RNAseqMotifs/HomerMotif_anno.csv"
rnaseqfile="/Volumes/Huitian/Exp174/NormalizedGeneCounts.csv"
intab=ascii.read(infile)
intab=fc.setcolnames(intab)
rtab=ascii.read(rnaseqfile)
rtab=fc.setcolnames(rtab)

ingenelist=list(intab["GeneName"])
rgenelist=list(rtab.columns[0])

inr=[]
for i in ingenelist:
    if i in rgenelist:
        inr.append("true")
    else:
        inr.append("false")

intab["InRNAseq"]=inr

ascii.write(intab,"HomerMotif_anno_RNAseq.csv", format="csv")



#####------------------ Main function END ------------------#####







































