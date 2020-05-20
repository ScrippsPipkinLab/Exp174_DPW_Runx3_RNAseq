#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 23:14:39 2017

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
wk_dir="/Volumes/Huitian/Exp174/1_Refseq/chr_split"

peak_file="/Volumes/Huitian/Exp174/1_Refseq/Exp122_Exp169_GSE88987_mergedPeaks_cord.csv"
ref_file="mm10_refseq_match_mg_e-100000.csv"

#####------------------ Config END ------------------#####



#####------------------ Self defined function START ------------------######
os.chdir(code_dir)
import fc_basic_astropy_subprocess as fc

###--- only works for increasing list
def first_larger(ele,a_list):
    for i in xrange(0, len(a_list)):
        if a_list[0] >= ele:
            return 0
        if i+1<len(a_list):
            if (a_list[i]<=ele and a_list[i+1]>=ele):
                return i+1
          
def last_smaller(ele,a_list):
    for i in xrange(0, len(a_list)):
        if i+1<len(a_list):
            if (a_list[i]<=ele and a_list[i+1]>=ele):
                return i
        else:
            return i
            
#####------------------ Self defined function END ------------------######


#####------------------ Main function START ------------------#####
os.chdir(wk_dir)

###----- Find gene name for each peak
#peak_file="/Volumes/Huitian/Exp174/1_Refseq/chr_split/chr1_peak_test.csv"
#ref_file="/Volumes/Huitian/Exp174/1_Refseq/chr_split/chr1_gene_test.csv"

def match_genes(peak_file,ref_file):
    peak_file_nf=fc.filenamenoformat(fc.Getfilename(peak_file))
    out_file_name="%s_ann.csv"%peak_file_nf

    ref_data=ascii.read(ref_file)
    ref_data.sort(["txStart","txEnd"])
    ref_data=fc.setcolnames(ref_data)
    ref_name_list=list(ref_data["gene_name"])
    ref_s_list=list(ref_data["txStart"])
    ref_e_list=list(ref_data["txEnd"])
    
    
    with open(out_file_name,"w") as fout:
        outwriter=csv.writer(fout, delimiter=",")  
        
        with open(peak_file,"r") as fin:
            inreader=csv.reader(fin,delimiter=",")
            
            in_colnames=next(inreader)
            in_colnames.append("gene_number")
            in_colnames.append("gene_name")
            outwriter.writerow(in_colnames)
            
            row_out=[]
            for row in inreader:
                row_out=row
                row_s=int(row[2])
                row_e=int(row[3])
                row_genelist=[]
                
                s_idx_1=last_smaller(row_s,ref_s_list)
                s_idx_2=first_larger(row_s,ref_e_list)
                
                e_idx_1=last_smaller(row_e,ref_s_list)
                e_idx_2=first_larger(row_e,ref_e_list)

                #print row
                #print ref_s_list
                #print ref_e_list
                
                #print index_1
                #print index_2
                #print '\n'
                
                id_1=min(s_idx_1,s_idx_2,e_idx_1,e_idx_2)
                id_2=max(s_idx_1,s_idx_2,e_idx_1,e_idx_2)
                if (id_1 != None and id_2 != None):
                    for idx in xrange(id_1, id_2+1):
                        if (ref_s_list[idx]<=row_s and ref_e_list[idx]>=row_e):
                            row_genelist.append(ref_name_list[idx])

                row_out.append(len(row_genelist))
                if len(row_genelist)>0:
                    row_out.append(",".join(row_genelist))
                else:
                    row_out.append("NA")
                outwriter.writerow(row_out)

peak_file_base="Exp122_Exp169_GSE88987_mergedPeaks_cord.csv"
ref_file_base="mm10_refseq_match_mg_e-100000.csv"

for chrn in xrange(1,20):
    pf_chrn="chr%s_%s"%(chrn,peak_file_base)
    rf_chrn="chr%s_%s"%(chrn,ref_file_base)
    match_genes(pf_chrn,rf_chrn)

match_genes("chrX_Exp122_Exp169_GSE88987_mergedPeaks_cord.csv","chrX_mm10_refseq_match_mg_e-100000.csv")


###----- Convert to a single file

all_chr_filename="Exp122_Exp169_GSE88987_mergedPeaks_cord_ann.csv"

with open(all_chr_filename,"w") as fout:
    outwriter=csv.writer(fout, delimiter=",")
    
    with open("chrX_Exp122_Exp169_GSE88987_mergedPeaks_cord_ann.csv","r") as fin:
        finreader=csv.reader(fin,delimiter=",")
        head=next(finreader)
        outwriter.writerow(head)      
        for row in finreader:
            outwriter.writerow(row)
            
    for x in xrange(1,20):
        finname="chr%s_Exp122_Exp169_GSE88987_mergedPeaks_cord_ann.csv"%x
        with open(finname,"r") as fin:
            finreader=csv.reader(fin,delimiter=",")
            head=next(finreader)
            for row in finreader:
                outwriter.writerow(row)

            





















