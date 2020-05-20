awk -F ',' '{if (NR==1) {print $0} else if ($3>0) {print $0}}'

awk -F ',' '{if (NR==1) {print $0} else if ($3<0) {print $0}}'
