require(MEGENA)
require(igraph)
library(knitr)

setwd("/Volumes/Huitian/Exp174")
input<-read.csv("RawGeneCounts.csv")
RNAseqfile<-input
siggenes<-read.csv("/Volumes/Huitian/Exp174/D8_MPEC_KO_vs_WT.csv")
siggenes<-subset(siggenes, padj<0.05)
siggenes<-as.factor(siggenes$X)
siggenes
willitwork<-subset(RNAseqfile,Gene %in% siggenes)
row.names(willitwork)<-willitwork$Gene
willitwork$Gene<-NULL