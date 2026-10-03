suppressPackageStartupMessages(library(DEXSeq))

stopifnot(packageVersion("DEXSeq") == "1.58.0")

set.seed(58)
sample_data <- data.frame(
  condition = factor(rep(c("control", "treated"), each = 3)),
  sample = factor(paste0("sample", 1:6)),
  row.names = paste0("sample", 1:6)
)
count_data <- matrix(
  rnbinom(72, mu = 80, size = 3),
  nrow = 12,
  dimnames = list(NULL, row.names(sample_data))
)
storage.mode(count_data) <- "integer"

dxd <- DEXSeqDataSet(
  countData = count_data,
  sampleData = sample_data,
  design = ~ sample + exon + condition:exon,
  featureID = rep(paste0("E", 1:3), 4),
  groupID = rep(paste0("gene", 1:4), each = 3)
)

stopifnot(
  nrow(dxd) == nrow(count_data),
  ncol(dxd) == 2L * nrow(sample_data),
  all(c("sample", "exon", "condition") %in% colnames(colData(dxd))),
  is.function(DEXSeq)
)
message("DEXSeq ", packageVersion("DEXSeq"), " smoke test passed")
