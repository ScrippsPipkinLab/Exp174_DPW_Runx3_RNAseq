#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 12:26:48 2017

@author: yolandatiao
"""

#####------------------ Import START ------------------#####
import os # For changing directory
import csv # For using csv writer
import string # For using string replace
from astropy.io import ascii # For using ascii table to open csv
from astropy.table import Table, Column, join   # For using astropy table functions
import glob # For finding filenames under a directory
#####------------------ Import END ------------------#####



#####------------------ Config START ------------------#####
code_dir="/Volumes/Huitian/Exp174/codes"
out_dir="/Volumes/Huitian/Exp174/0_DEseq/slt_genename_list"
in_dir="/Volumes/Huitian/Exp174/0_DEseq/padjsig0.05"
refseq="/Volumes/Huitian/Exp174/mm10_refseq_match.csv"
expand=100000
#####------------------ Config END ------------------#####



#####------------------ Self defined function START ------------------######
os.chdir(code_dir)
import fc_basic_astropy_subprocess as fc
#####------------------ Self defined function END ------------------######



#####------------------ Main function START ------------------#####

###----- I Transform data to selected gene name list
'''
def slt_list(in_file):
    in_data=ascii.read(in_file)
    in_data=fc.setcolnames(in_data)
    out_data=Table()
    out_data["gene_name"]=in_data.columns[0]
    return out_data
file_all=[]
os.chdir(in_dir)
for file in glob.glob("*.csv"):
    file_all.append(file)
for i in file_all:
    os.chdir(in_dir)
    i_name=fc.filenamenoformat(fc.Getfilename(i))
    out_i=slt_list(i)
    os.chdir(out_dir)
    ascii.write(out_i,"%s_gn.csv"%i_name, format="csv", overwrite=True)
'''

###----- II Merge ranked refseq file genes (exons merge into one large coordinate range)
'''
os.chdir("/Volumes/Huitian/Exp174")
in_file="mm10_refseq_match.csv"
with open(in_file,"r") as inputfile:
    in_file_nf=fc.filenamenoformat(fc.Getfilename(in_file))
    read_in=csv.reader(inputfile,delimiter=",")
    
    out_filename="%s_mg.csv"%in_file_nf
    with open(out_filename, "w") as fout:
        foutwriter=csv.writer(fout, delimiter=",")        
        in_colnames=next(read_in)
        foutwriter.writerow(in_colnames)
        
        firstR=next(read_in)
        name_x=firstR[0]
        chrom_x=firstR[1]
        txStart=firstR[2]
        txEnd=firstR[3]
        new_row=[]
        for row in read_in:
            #print row
            if name_x==row[0] and chrom_x==row[1]:
                #print "repeat gene"
                #print row[2]
                #print txStart
                if int(row[2])<int(txStart):
                    txStart=row[2]
                    #print row[2]
                    #print txStart
                    #print "new start"
                if int(row[3])>int(txEnd):
                    txEnd=row[3]
                    #print "new end"
            else:
                new_row=[name_x,chrom_x,txStart,txEnd]
                foutwriter.writerow(new_row)
                name_x=row[0]
                chrom_x=row[1]
                txStart=row[2]
                txEnd=row[3]
                new_row=[name_x,chrom_x,txStart,txEnd]
            #print "\n"
        foutwriter.writerow(new_row)
'''

###----- Expand coordinates
'''
ref_mg="/Volumes/Huitian/Exp174/mm10_refseq_match_mg.csv"
ref_mg_nf=fc.filenamenoformat(fc.Getfilename(ref_mg))
ref_mg_exp_name="%s_e-%s.csv"%(ref_mg_nf,expand)

ref_mg_tab=ascii.read(ref_mg)
ref_mg_tab=fc.setcolnames(ref_mg_tab)

ref_mg_s=list(ref_mg_tab["txStart"])
ref_mg_e=list(ref_mg_tab["txEnd"])

ref_mg_s_exp=[]
ref_mg_e_exp=[]

for i in ref_mg_s:
    if int(i)-expand > 0:
        ref_mg_s_exp.append(int(i)-expand)
    else:
        ref_mg_s_exp.append(0)

for i in ref_mg_e:
    ref_mg_e_exp.append(int(i)+expand)
    
ref_mg_exp_tab=ref_mg_tab
ref_mg_exp_tab["txStart"]=ref_mg_s_exp
ref_mg_exp_tab["txEnd"]=ref_mg_e_exp

ascii.write(ref_mg_exp_tab,ref_mg_exp_name, format="csv", overwrite=True)
'''

    
#####------------------ Main function END ------------------#####













