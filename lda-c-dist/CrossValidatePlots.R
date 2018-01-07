library(ggplot2)
library(matrixStats)
library(Hmisc)

setwd('Documents/PrincetonJunior/COS424/FinalProject/lda-c-dist')

likelihoods = matrix(nrow = 0,ncol = 0)
numtopics = c()
#read 
for (i in 3:9) {
  row = read.table(paste0('likelihood', i, '.txt'), sep=',')[1:5]
  likelihoods = rbind(likelihoods,row)
  numtopics = append(numtopics,i)
}

average = rowMeans(likelihoods)
SD = rowSds(likelihoods)
SE = SD/sqrt(5)

data=data.frame(x=numtopics,y=average,sd=SE)
plot(data$x,data$y,type="l",ylim = c(-115000,-95000),xlab = "Number of Topics",ylab = "Held-out log likelihood")
with (
  data = data, expr = errbar(x, y, y+sd, y-sd, add=T, pch=1, cap=.1)
)
title(main="LDA Five-Fold Cross Validation")
