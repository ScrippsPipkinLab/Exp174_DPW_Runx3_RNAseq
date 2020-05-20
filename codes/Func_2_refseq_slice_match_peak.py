#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:09:26 2017

@author: yolandatiao
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 21:27:22 2017

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
wk_dir="/Volumes/Huitian/Exp174/1_Refseq"

peak_file="/Volumes/Huitian/Exp174/1_Refseq/Exp122_Exp169_GSE88987_mergedPeaks_cord.csv"
ref_file="mm10_refseq_match_mg_e-100000.csv"

#####------------------ Config END ------------------#####



#####------------------ Self defined function START ------------------######
os.chdir(code_dir)
import fc_basic_astropy_subprocess as fc
#####------------------ Self defined function END ------------------######


#####------------------ Main function START ------------------#####
os.chdir(wk_dir)

###----- Slice data tables
'''
peak_filename_nf=fc.filenamenoformat(fc.Getfilename(peak_file))
ref_filename_nf=fc.filenamenoformat(fc.Getfilename(ref_file))

peak_data=ascii.read(peak_file)
ref_data=ascii.read(ref_file)

peak_data=fc.setcolnames(peak_data)
ref_data=fc.setcolnames(ref_data)

peak_data.sort(["chr","start","end"])
ref_data.sort(["chrom","txStart","txEnd"])

peak_data_chrlist=list(peak_data["chr"])
ref_data_chrlist=list(ref_data["chrom"])


peak_data_chrset=sorted(list(set(peak_data_chrlist)))
ref_data_chrset=sorted(list(set(ref_data_chrlist)))


for n in xrange(0,len(peak_data_chrset)):
    chr_n=peak_data_chrset[n]
    peak_data_n_index=peak_data_chrlist.index(chr_n)
    
    if n < (len(peak_data_chrset)-1):        
        chr_n1=peak_data_chrset[n+1]
        peak_data_n1_index=peak_data_chrlist.index(chr_n1)
    else:
        peak_data_n1_index=len(peak_data_chrlist)+1
    
    peak_data_chrn=peak_data[peak_data_n_index:peak_data_n1_index]
    ascii.write(peak_data_chrn,"%s_%s.csv"%(chr_n,peak_filename_nf), format="csv", overwrite=True)
    
for n in xrange(0,len(ref_data_chrset)):
    chr_n=ref_data_chrset[n]
    ref_data_n_index=ref_data_chrlist.index(chr_n)
    
    if n < (len(ref_data_chrset)-1):        
        chr_n1=ref_data_chrset[n+1]
        ref_data_n1_index=ref_data_chrlist.index(chr_n1)
    else:
        ref_data_n1_index=len(ref_data_chrlist)+1
    
    ref_data_chrn=ref_data[ref_data_n_index:ref_data_n1_index]
    ascii.write(ref_data_chrn,"%s_%s.csv"%(chr_n,ref_filename_nf), format="csv", overwrite=True)
'''



###----- Find gene name for each peak
peak_file="/Volumes/Huitian/Exp174/1_Refseq/chr_split/chr1_Exp122_Exp169_GSE88987_mergedPeaks_cord.csv"
ref_file="/Volumes/Huitian/Exp174/1_Refseq/chr_split/chr1_mm10_refseq_match_mg_e-100000.csv"

peak_file_nf=fc.filenamenoformat(fc.Getfilename(peak_file))
ref_file_nf=fc.filenamenoformat(fc.Getfilename(ref_file))
out_file_name="%s_ann-%s.csv"%(peak_file_nf,ref_file_nf)

ref_data=ascii.read(ref_file)
ref_data=fc.setcolnames(ref_data)
ref_data_len=len(ref_data)

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
            row_chr=row[1]
            row_s=row[2]
            row_e=row[3]
            row_genelist=[]
            ref_data_x=[]
            for x in xrange(0, ref_data_len):
                ref_data_x=list(ref_data[x])
                if ref_data_x[1]==row_chr:
                    if (ref_data_x[2]<=row_s and ref_data_x[3]>row_e):
                        row_genelist.append(ref_data[0])
            
            row_out.append(len(row_genelist))
            if len(row_genelist)>0:
                row_out.append(",".join(row_genelist))
            else:
                row_out.append("NA")
            outwriter.writerow(row_out)

                
                    
            

   
#####------------------ Main function END ------------------#####