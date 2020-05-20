#!/bin/bash

cd /Volumes/Huitian/Exp174/0_DEseq

awk -F ',' '{if (NR==1) {print $0} else if ($7<0.1) {print $0}}' KO-Day5-EEC_VS_WT-Day5-EEC.csv > KO-Day5-EEC_VS_WT-Day5-EEC.csv_padjsig0_1.csv
awk -F ',' '{if (NR==1) {print $0} else if ($7<0.05) {print $0}}' KO-Day5-EEC_VS_WT-Day5-EEC.csv > KO-Day5-EEC_VS_WT-Day5-EEC.csv_padjsig0_05.csv
awk -F ',' '{if (NR==1) {print $0} else if ($7<0.01) {print $0}}' KO-Day5-EEC_VS_WT-Day5-EEC.csv > KO-Day5-EEC_VS_WT-Day5-EEC.csv_padjsig0_01.csv
awk -F ',' '{if (NR==1) {print $0} else if ($7<0.001) {print $0}}' KO-Day5-EEC_VS_WT-Day5-EEC.csv > KO-Day5-EEC_VS_WT-Day5-EEC.csv_padjsig0_001.csv

awk -F ',' '{if (NR==1) {print $0} else if ($6<0.1) {print $0}}' KO-Day5-EEC_VS_WT-Day5-EEC.csv > KO-Day5-EEC_VS_WT-Day5-EEC.csv_pvaluesig0_1.csv
awk -F ',' '{if (NR==1) {print $0} else if ($6<0.05) {print $0}}' KO-Day5-EEC_VS_WT-Day5-EEC.csv > KO-Day5-EEC_VS_WT-Day5-EEC.csv_pvaluesig0_05.csv
awk -F ',' '{if (NR==1) {print $0} else if ($6<0.01) {print $0}}' KO-Day5-EEC_VS_WT-Day5-EEC.csv > KO-Day5-EEC_VS_WT-Day5-EEC.csv_pvaluesig0_01.csv
awk -F ',' '{if (NR==1) {print $0} else if ($6<0.001) {print $0}}' KO-Day5-EEC_VS_WT-Day5-EEC.csv > KO-Day5-EEC_VS_WT-Day5-EEC.csv_pvaluesig0_001.csv

awk -F ',' '{if (NR==1) {print $0} else if ($7<0.1) {print $0}}' KO-Day5-SLEC_VS_WT-Day5-SLEC.csv > KO-Day5-SLEC_VS_WT-Day5-SLEC.csv_padjsig0_1.csv
awk -F ',' '{if (NR==1) {print $0} else if ($7<0.05) {print $0}}' KO-Day5-SLEC_VS_WT-Day5-SLEC.csv > KO-Day5-SLEC_VS_WT-Day5-SLEC.csv_padjsig0_05.csv
awk -F ',' '{if (NR==1) {print $0} else if ($7<0.01) {print $0}}' KO-Day5-SLEC_VS_WT-Day5-SLEC.csv > KO-Day5-SLEC_VS_WT-Day5-SLEC.csv_padjsig0_01.csv
awk -F ',' '{if (NR==1) {print $0} else if ($7<0.001) {print $0}}' KO-Day5-SLEC_VS_WT-Day5-SLEC.csv > KO-Day5-SLEC_VS_WT-Day5-SLEC.csv_padjsig0_001.csv

awk -F ',' '{if (NR==1) {print $0} else if ($6<0.1) {print $0}}' KO-Day5-SLEC_VS_WT-Day5-SLEC.csv > KO-Day5-SLEC_VS_WT-Day5-SLEC.csv_pvaluesig0_1.csv
awk -F ',' '{if (NR==1) {print $0} else if ($6<0.05) {print $0}}' KO-Day5-SLEC_VS_WT-Day5-SLEC.csv > KO-Day5-SLEC_VS_WT-Day5-SLEC.csv_pvaluesig0_05.csv
awk -F ',' '{if (NR==1) {print $0} else if ($6<0.01) {print $0}}' KO-Day5-SLEC_VS_WT-Day5-SLEC.csv > KO-Day5-SLEC_VS_WT-Day5-SLEC.csv_pvaluesig0_01.csv
awk -F ',' '{if (NR==1) {print $0} else if ($6<0.001) {print $0}}' KO-Day5-SLEC_VS_WT-Day5-SLEC.csv > KO-Day5-SLEC_VS_WT-Day5-SLEC.csv_pvaluesig0_001.csv

awk -F ',' '{if (NR==1) {print $0} else if ($7<0.1) {print $0}}' KO-Day8-EEC_VS_WT-Day8-EEC.csv > KO-Day8-EEC_VS_WT-Day8-EEC.csv_padjsig0_1.csv
awk -F ',' '{if (NR==1) {print $0} else if ($7<0.05) {print $0}}' KO-Day8-EEC_VS_WT-Day8-EEC.csv > KO-Day8-EEC_VS_WT-Day8-EEC.csv_padjsig0_05.csv
awk -F ',' '{if (NR==1) {print $0} else if ($7<0.01) {print $0}}' KO-Day8-EEC_VS_WT-Day8-EEC.csv > KO-Day8-EEC_VS_WT-Day8-EEC.csv_padjsig0_01.csv
awk -F ',' '{if (NR==1) {print $0} else if ($7<0.001) {print $0}}' KO-Day8-EEC_VS_WT-Day8-EEC.csv > KO-Day8-EEC_VS_WT-Day8-EEC.csv_padjsig0_001.csv

awk -F ',' '{if (NR==1) {print $0} else if ($6<0.1) {print $0}}' KO-Day8-EEC_VS_WT-Day8-EEC.csv > KO-Day8-EEC_VS_WT-Day8-EEC.csv_pvaluesig0_1.csv
awk -F ',' '{if (NR==1) {print $0} else if ($6<0.05) {print $0}}' KO-Day8-EEC_VS_WT-Day8-EEC.csv > KO-Day8-EEC_VS_WT-Day8-EEC.csv_pvaluesig0_05.csv
awk -F ',' '{if (NR==1) {print $0} else if ($6<0.01) {print $0}}' KO-Day8-EEC_VS_WT-Day8-EEC.csv > KO-Day8-EEC_VS_WT-Day8-EEC.csv_pvaluesig0_01.csv
awk -F ',' '{if (NR==1) {print $0} else if ($6<0.001) {print $0}}' KO-Day8-EEC_VS_WT-Day8-EEC.csv > KO-Day8-EEC_VS_WT-Day8-EEC.csv_pvaluesig0_001.csv

awk -F ',' '{if (NR==1) {print $0} else if ($7<0.1) {print $0}}' KO-Day8-MPEC_VS_WT-Day8-MPEC.csv > KO-Day8-MPEC_VS_WT-Day8-MPEC.csv_padjsig0_1.csv
awk -F ',' '{if (NR==1) {print $0} else if ($7<0.05) {print $0}}' KO-Day8-MPEC_VS_WT-Day8-MPEC.csv > KO-Day8-MPEC_VS_WT-Day8-MPEC.csv_padjsig0_05.csv
awk -F ',' '{if (NR==1) {print $0} else if ($7<0.01) {print $0}}' KO-Day8-MPEC_VS_WT-Day8-MPEC.csv > KO-Day8-MPEC_VS_WT-Day8-MPEC.csv_padjsig0_01.csv
awk -F ',' '{if (NR==1) {print $0} else if ($7<0.001) {print $0}}' KO-Day8-MPEC_VS_WT-Day8-MPEC.csv > KO-Day8-MPEC_VS_WT-Day8-MPEC.csv_padjsig0_001.csv

awk -F ',' '{if (NR==1) {print $0} else if ($6<0.1) {print $0}}' KO-Day8-MPEC_VS_WT-Day8-MPEC.csv > KO-Day8-MPEC_VS_WT-Day8-MPEC.csv_pvaluesig0_1.csv
awk -F ',' '{if (NR==1) {print $0} else if ($6<0.05) {print $0}}' KO-Day8-MPEC_VS_WT-Day8-MPEC.csv > KO-Day8-MPEC_VS_WT-Day8-MPEC.csv_pvaluesig0_05.csv
awk -F ',' '{if (NR==1) {print $0} else if ($6<0.01) {print $0}}' KO-Day8-MPEC_VS_WT-Day8-MPEC.csv > KO-Day8-MPEC_VS_WT-Day8-MPEC.csv_pvaluesig0_01.csv
awk -F ',' '{if (NR==1) {print $0} else if ($6<0.001) {print $0}}' KO-Day8-MPEC_VS_WT-Day8-MPEC.csv > KO-Day8-MPEC_VS_WT-Day8-MPEC.csv_pvaluesig0_001.csv

awk -F ',' '{if (NR==1) {print $0} else if ($7<0.1) {print $0}}' KO-Day8-SLEC_VS_WT-Day8-SLEC.csv > KO-Day8-SLEC_VS_WT-Day8-SLEC.csv_padjsig0_1.csv
awk -F ',' '{if (NR==1) {print $0} else if ($7<0.05) {print $0}}' KO-Day8-SLEC_VS_WT-Day8-SLEC.csv > KO-Day8-SLEC_VS_WT-Day8-SLEC.csv_padjsig0_05.csv
awk -F ',' '{if (NR==1) {print $0} else if ($7<0.01) {print $0}}' KO-Day8-SLEC_VS_WT-Day8-SLEC.csv > KO-Day8-SLEC_VS_WT-Day8-SLEC.csv_padjsig0_01.csv
awk -F ',' '{if (NR==1) {print $0} else if ($7<0.001) {print $0}}' KO-Day8-SLEC_VS_WT-Day8-SLEC.csv > KO-Day8-SLEC_VS_WT-Day8-SLEC.csv_padjsig0_001.csv

awk -F ',' '{if (NR==1) {print $0} else if ($6<0.1) {print $0}}' KO-Day8-SLEC_VS_WT-Day8-SLEC.csv > KO-Day8-SLEC_VS_WT-Day8-SLEC.csv_pvaluesig0_1.csv
awk -F ',' '{if (NR==1) {print $0} else if ($6<0.05) {print $0}}' KO-Day8-SLEC_VS_WT-Day8-SLEC.csv > KO-Day8-SLEC_VS_WT-Day8-SLEC.csv_pvaluesig0_05.csv
awk -F ',' '{if (NR==1) {print $0} else if ($6<0.01) {print $0}}' KO-Day8-SLEC_VS_WT-Day8-SLEC.csv > KO-Day8-SLEC_VS_WT-Day8-SLEC.csv_pvaluesig0_01.csv
awk -F ',' '{if (NR==1) {print $0} else if ($6<0.001) {print $0}}' KO-Day8-SLEC_VS_WT-Day8-SLEC.csv > KO-Day8-SLEC_VS_WT-Day8-SLEC.csv_pvaluesig0_001.csv

