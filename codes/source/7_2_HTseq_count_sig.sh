awk -F ',' '{if (NR==1) {print $0} else if ($7<0.1) {print $0}}' inputfile > inputfile_padjsig0_1.csv
awk -F ',' '{if (NR==1) {print $0} else if ($7<0.05) {print $0}}' inputfile > inputfile_padjsig0_05.csv
awk -F ',' '{if (NR==1) {print $0} else if ($7<0.01) {print $0}}' inputfile > inputfile_padjsig0_01.csv
awk -F ',' '{if (NR==1) {print $0} else if ($7<0.001) {print $0}}' inputfile > inputfile_padjsig0_001.csv

awk -F ',' '{if (NR==1) {print $0} else if ($6<0.1) {print $0}}' inputfile > inputfile_pvaluesig0_1.csv
awk -F ',' '{if (NR==1) {print $0} else if ($6<0.05) {print $0}}' inputfile > inputfile_pvaluesig0_05.csv
awk -F ',' '{if (NR==1) {print $0} else if ($6<0.01) {print $0}}' inputfile > inputfile_pvaluesig0_01.csv
awk -F ',' '{if (NR==1) {print $0} else if ($6<0.001) {print $0}}' inputfile > inputfile_pvaluesig0_001.csv
