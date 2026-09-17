#!/usr/bin/env Rscript
args <- commandArgs(trailingOnly = TRUE)
stopifnot(length(args) == 2)
source(file.path(Sys.getenv('DRUID_HOME', '/opt/DRUID'), 'DRUID.R'))
samples <- read.delim(args[2], check.names = FALSE, stringsAsFactors = FALSE)
samples <- samples[order(samples$time_hours), ]
stopifnot(!anyDuplicated(samples$sample), !anyDuplicated(samples$time_hours))
setwd(args[1])
times <- samples$time_hours
htseq <- read.delim('htseq_exons_introns/combined_exon.txt', check.names = FALSE)
stopifnot(all(samples$sample %in% names(htseq)))
get_counts <- function(organism) {
  selected <- htseq$Organism == organism
  counts <- htseq[selected, samples$sample, drop = FALSE]
  rownames(counts) <- htseq$Gene[selected]
  Filter(counts)
}
data.reads <- get_counts('h')
spike.reads <- get_counts('f')
if (nrow(data.reads) < 2 || nrow(spike.reads) < 1) stop('Insufficient human or fly genes passing the tutorial expression filter')
logs <- read.table('Logs/Logs.tsv', col.names = c('Sample','Input','Unique','Multi','TooMany'))
stopifnot(!anyDuplicated(logs$Sample))
library.sizes <- logs$Unique[match(samples$sample, logs$Sample)]
if (anyNA(library.sizes) || any(library.sizes <= 0)) stop('Missing or zero uniquely mapped read counts')
# Explicit sample/type order avoids lexical time-point and filesystem-order errors.
csvs <- unlist(lapply(samples$sample, function(sample) {
  file.path('intersect', paste0(sample, c('_exon_neg.csv','_exon_pos.csv','_intron_neg.csv','_intron_pos.csv')))
}))
stopifnot(all(file.exists(csvs)))
suffixes <- paste0('.', times)
exons.all <- rbind(ExtractAndMerge(csvs, 4, 0, suffixes), ExtractAndMerge(csvs, 4, 1, suffixes))
introns.all <- rbind(ExtractAndMerge(csvs, 4, 2, suffixes), ExtractAndMerge(csvs, 4, 3, suffixes))
introns.human <- introns.all[introns.all$organism == 'h', ]
coverage <- as.matrix(introns.human[, grep('^mean\\.', names(introns.human)), drop=FALSE])
eligible <- complete.cases(coverage) & apply(coverage, 1, function(x) all(x >= 0.5))
if (sum(eligible) < 5) stop('Fewer than five introns pass the coverage threshold; more reads or suitable introns are required')
spike.norm <- colSums(spike.reads)
stopifnot(all(is.finite(spike.norm)), all(spike.norm > 0))
half.lives.spikeins <- LeaveOneOut(times, data.reads, spike.norm, HalfLives4SU)
half.lives.DRUID <- DRUID(x=times, introns=introns.human, data=data.reads,
                        lib.sizes=library.sizes, path='DRUID.replicate.1', kmeans.seed=42)
write.csv(half.lives.spikeins, 'half-lives.spikeins.csv')
write.csv(half.lives.DRUID, 'half-lives.DRUID.csv')
saveRDS(list(samples=samples, library.sizes=library.sizes, data.reads=data.reads,
             spike.reads=spike.reads, exons=exons.all, introns=introns.all,
             half.lives.DRUID=half.lives.DRUID, half.lives.spikeins=half.lives.spikeins),
        'analysis.rds')
writeLines(capture.output(sessionInfo()), 'R-sessionInfo.txt')
cat('Saved half-lives, heatmap, intron normalization counts, and analysis.rds\n')
