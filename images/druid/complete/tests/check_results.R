args <- commandArgs(trailingOnly=TRUE)
a <- readRDS(file.path(args[1], 'Analysis/HEK293_R1/analysis.rds'))
stopifnot(ncol(a$half.lives.DRUID)==7, nrow(a$half.lives.DRUID)==48,
          sum(is.finite(a$half.lives.DRUID[,1])) > 30,
          nrow(a$half.lives.spikeins)==48,
          all(a$library.sizes > 0), nrow(a$introns)==60)
source('/opt/DRUID/DRUID.R')
x <- c(1,2,4,8,12,24)
y <- 100 * (1-exp(-log(2)*x/3))
stopifnot(abs(HalfLives4SU(x,y,doubling.time=0)-3) < 1e-4)
# Changing sequencing depth per sample must preserve clustering and half-lives.
introns <- a$introns[a$introns$organism=='h',]
original <- DRUID(x, introns, a$data.reads, a$library.sizes,
                  tempfile(), plot=FALSE, kmeans.seed=42)
factors <- c(2,5,3,4,7,6)
mi <- grep('^mean\\.',names(introns))
introns[,mi] <- sweep(introns[,mi],2,factors,'*')
scaled <- DRUID(x, introns, sweep(a$data.reads,2,factors,'*'), a$library.sizes*factors,
                tempfile(), plot=FALSE, kmeans.seed=42)
stopifnot(isTRUE(all.equal(original,scaled,tolerance=1e-5)))
cat('PASS: end-to-end outputs, known half-life, and sequencing-depth invariance\n')
